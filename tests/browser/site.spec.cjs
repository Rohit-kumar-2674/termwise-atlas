const {test,expect} = require('@playwright/test');
const AxeBuilder = require('@axe-core/playwright').default;
const fs = require('node:fs');

test('chooser works across routes; no model or third-party requests', async ({page})=>{
  const failures=[]; const remote=[];
  page.on('pageerror',error=>failures.push(error.message));
  page.on('request',request=>{if(!request.url().startsWith('http://127.0.0.1:8765') && !request.url().startsWith('data:')) remote.push(request.url());});
  await page.goto('/');
  await expect(page.locator('.atlas-result')).toHaveAttribute('data-route','android-cloud');
  await page.getByLabel('2. Your goal').selectOption('local');
  await expect(page.locator('.atlas-result')).toHaveAttribute('data-route','android-local');
  await page.getByLabel('1. Your device').selectOption('linux');
  await page.getByLabel('3. Installed memory').selectOption('32');
  await expect(page.locator('.atlas-result')).toHaveAttribute('data-route','local');
  await page.getByRole('link',{name:'Open the guide →',exact:true}).click();
  await expect(page).toHaveURL(/providers\/ollama\/$/);
  expect(failures).toEqual([]);expect(remote).toEqual([]);
});

test('compatibility filters have working empty and reset states', async ({page})=>{
  await page.goto('/getting-started/comparison/');
  await expect(page.locator('.atlas-tool')).toHaveCount(9);
  await page.getByLabel('Model route').selectOption('local');
  await expect(page.locator('.atlas-tool')).toHaveCount(6);
  await page.getByLabel('Search tools').fill('no-such-tool');
  await expect(page.locator('.atlas-empty')).toContainText('No matching');
  await page.getByLabel('Search tools').fill('');
  await page.getByLabel('Model route').selectOption('free');
  await expect(page.locator('.atlas-tool')).toHaveCount(2);
  await page.getByLabel('Platform evidence').selectOption('android');
  await expect(page.locator('.atlas-tool')).toHaveCount(1);
  await expect(page.locator('.atlas-tool h3')).toContainText('OpenRouter');
});

test('mobile navigation, theme, overflow, and accessible widgets', async ({page})=>{
  await page.setViewportSize({width:390,height:844});
  await page.goto('/');
  await expect(page.locator('.atlas-result')).toBeVisible();
  await page.locator('label.md-header__button[for="__drawer"]').click();
  await expect(page.locator('#__drawer')).toBeChecked();
  await page.locator('label.md-overlay').click({position:{x:380,y:700}});
  await page.locator('label[title="Switch to dark mode"]').click();
  await expect(page.locator('body')).toHaveAttribute('data-md-color-scheme','slate');
  await page.locator('label[title="Switch to light mode"]').click();
  const overflow=await page.evaluate(()=>document.documentElement.scrollWidth>window.innerWidth);
  expect(overflow).toBe(false);
  const a11y=await new AxeBuilder({page}).include('#setup-chooser').analyze();
  expect(a11y.violations).toEqual([]);
  fs.mkdirSync('.qa/screenshots',{recursive:true});
  await page.screenshot({path:'.qa/screenshots/mobile-home.png',fullPage:true});
});

test('desktop layout, copy controls, and search', async ({page})=>{
  await page.setViewportSize({width:1440,height:1000});
  await page.goto('/');
  await expect(page.locator('.atlas-result')).toBeVisible();
  const a11y=await new AxeBuilder({page}).include('.md-content').analyze();
  expect(a11y.violations).toEqual([]);
  fs.mkdirSync('.qa/screenshots',{recursive:true});
  await page.screenshot({path:'.qa/screenshots/desktop-home.png',fullPage:true});
  await page.goto('/providers/ollama/');
  await expect(page.getByRole('button',{name:'Copy to clipboard',exact:true}).first()).toBeVisible();
  await page.getByRole('textbox',{name:'Search',exact:true}).fill('Termux');
  await expect(page.locator('.md-search-result__list')).toContainText('Termux');
});

test('text decision guide still works without JavaScript', async ({browser})=>{
  const context=await browser.newContext({javaScriptEnabled:false,viewport:{width:360,height:800}});
  const page=await context.newPage();
  await page.goto('/getting-started/choose/');
  await expect(page.getByRole('heading',{name:/Choose without JavaScript/})).toBeVisible();
  await expect(page.getByRole('link',{name:'Android + browser/SSH',exact:true})).toBeVisible();
  await context.close();
});
