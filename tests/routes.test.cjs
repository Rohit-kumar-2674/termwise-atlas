const test = require('node:test');
const assert = require('node:assert/strict');
const {execFileSync} = require('node:child_process');
const path = require('node:path');
const data = require('../data/routes.json');
const {chooseRoute} = require('../docs/assets/route-engine.js');
test('browser and Python wizard agree for every documented input', () => {
  const root=path.resolve(__dirname,'..');
  const code="import sys,json; sys.path.insert(0,'scripts'); import wizard; d=wizard.load_routes(); print(json.dumps([wizard.choose_route(p,g,r)['id'] for p in d['platforms'] for g in d['goals'] for r in d['ram_choices']]))";
  const expected=JSON.parse(execFileSync(process.env.PYTHON || 'python', ['-c',code],{cwd:root,encoding:'utf8'}));
  const actual=[];
  for (const p of data.platforms) for (const g of data.goals) for(const r of data.ram_choices) actual.push(chooseRoute(data,p,g,r).id);
  assert.deepEqual(actual,expected);
  assert.equal(new Set(actual).size,data.routes.length);
});
test('unknown input never silently suggests a paid or unsupported route',()=>{
  assert.throws(()=>chooseRoute(data,'android','bypass',4));
  assert.throws(()=>chooseRoute(data,'linux','local',0));
});
