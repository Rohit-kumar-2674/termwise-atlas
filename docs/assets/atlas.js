(function () {
  'use strict';
  const assetBase = new URL('.', document.currentScript.src);
  const siteBase = new URL('../', assetBase);
  const pathUrl = path => new URL(path.replace(/\.md$/, '/'), siteBase).href;
  const el = (tag, className, text) => {
    const node = document.createElement(tag);
    if (className) node.className = className;
    if (text !== undefined) node.textContent = text;
    return node;
  };
  function field(parent, id, label, options) {
    const wrap = el('div', 'atlas-field');
    const caption = el('label', '', label); caption.htmlFor = id;
    const select = el('select'); select.id = id;
    for (const [value, text] of options) { const item = el('option', '', text); item.value = value; select.append(item); }
    wrap.append(caption, select); parent.append(wrap); return select;
  }
  function link(label, path) { const a = el('a', '', label); a.href = pathUrl(path); return a; }
  async function getData(name) {
    const response = await fetch(new URL(name + '.json', assetBase));
    if (!response.ok) throw new Error('Data not available');
    return response.json();
  }
  async function chooser(node) {
    const data = await getData('routes');
    const fields = el('div', 'atlas-fields');
    const labels = {windows:'Windows',linux:'Linux',macos:'macOS',android:'Android phone',chromeos:'Chromebook',cloud:'Cloud terminal'};
    const goals = {local:'Keep inference local',cloud:'Use a cloud provider',free:'Find a free cloud allowance',multi:'Choose multiple models'};
    const device = field(fields, 'setup-platform', '1. Your device', data.platforms.map(x => [x,labels[x]]));
    const goal = field(fields, 'setup-goal', '2. Your goal', data.goals.map(x => [x,goals[x]]));
    const ram = field(fields, 'setup-ram', '3. Installed memory', data.ram_choices.map(x => [String(x),x+' GB'+(x===4?' / unsure':'')]));
    device.value = 'android'; goal.value = 'cloud'; ram.value = '4';
    const result = el('div', 'atlas-result'); result.setAttribute('aria-live', 'polite'); result.setAttribute('aria-atomic', 'true');
    function update() {
      const route = window.TermwiseRoutes.chooseRoute(data, device.value, goal.value, Number(ram.value));
      result.dataset.route = route.id;
      const links = el('div', 'atlas-result-links'); links.append(link('Open the guide →', route.guide),link('Then explore →', route.next));
      result.replaceChildren(el('h3', '', route.title),el('p', '', route.summary),el('p', 'atlas-cost', route.cost),links);
    }
    for (const input of [device,goal,ram]) input.addEventListener('change', update);
    node.replaceChildren(fields,result); update();
  }
  async function catalog(node) {
    const data = await getData('catalog');
    const fields = el('div', 'atlas-fields');
    const searchWrap = el('div', 'atlas-field'); const label = el('label','','Search tools'); label.htmlFor='tool-search';
    const search = el('input'); search.id='tool-search'; search.type='search'; search.placeholder='Name, license, provider…'; searchWrap.append(label,search); fields.append(searchWrap);
    const mode = field(fields,'tool-mode','Model route',[['all','All routes'],['local','Local inference'],['openrouter','OpenRouter integration'],['free','Explicit free-tier label']]);
    const platform = field(fields,'tool-platform','Platform evidence',[['all','All platforms'],['windows','Windows'],['linux','Linux'],['macos','macOS'],['android','Android (check caveats)'],['cloud','Cloud / Linux host']]);
    const count = el('p','atlas-count'); count.setAttribute('role','status');
    const cards = el('div','atlas-cards');
    function update() {
      const query = search.value.trim().toLocaleLowerCase();
      const filtered = data.tools.filter(t => {
        const haystack = [t.name,t.license,t.model_cost,t.openrouter,t.ollama,...t.labels].join(' ').toLocaleLowerCase();
        const modeMatch = mode.value==='all' || (mode.value==='local' && t.local) || (mode.value==='free' && t.labels.includes('FREE TIER')) || (mode.value==='openrouter' && !['Not established','Not a model-routing client'].includes(t.openrouter));
        return haystack.includes(query) && modeMatch && (platform.value==='all' || t.platforms[platform.value]!=='Not established');
      });
      count.textContent = filtered.length+' of '+data.tools.length+' entries · Source reviewed '+data.verified_on+'. Platform labels describe evidence, not universal runtime testing.';
      cards.replaceChildren();
      for (const t of filtered) {
        const card = el('article','atlas-tool'); const heading = el('h3'); heading.append(link(t.name,t.guide));
        const badges = el('div','atlas-badges'); for (const value of t.labels) badges.append(el('span','atlas-badge',value));
        card.append(heading,badges,el('p','',t.model_cost),el('p','','OpenRouter: '+t.openrouter),el('p','','Ollama: '+t.ollama));
        if(platform.value!=='all') card.append(el('p','',platform.options[platform.selectedIndex].text+': '+t.platforms[platform.value]));
        card.append(el('p','atlas-meta',t.license+' · Reviewed '+t.last_verified)); cards.append(card);
      }
      if (!filtered.length) cards.append(el('p','atlas-empty','No matching entries. Clear search or select another route.'));
    }
    search.addEventListener('input',update);mode.addEventListener('change',update);platform.addEventListener('change',update);
    node.replaceChildren(fields,count,cards);update();
  }
  function start() {
    for(const [id, init] of [['setup-chooser',chooser],['compatibility-browser',catalog]]) {
      const node=document.getElementById(id); if(node) init(node).catch(()=>node.replaceChildren(el('p','atlas-widget-error','Interactive data could not load. The text guide below remains available; serve this site over HTTP rather than opening a file URL.')));
    }
  }
  if(document.readyState==='loading') document.addEventListener('DOMContentLoaded',start); else start();
})();
