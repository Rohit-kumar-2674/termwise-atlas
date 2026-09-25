import test from 'node:test';
import assert from 'node:assert/strict';
import {toggleTask, progress} from './tasks.js';
test('toggle changes the selected task without mutating input', () => {
  const input = [{id:1,done:false},{id:2,done:true}];
  assert.deepEqual(toggleTask(input,1),[{id:1,done:true},{id:2,done:true}]);
  assert.equal(input[0].done,false);
  assert.deepEqual(toggleTask(input,99),input);
});
test('progress handles empty and partially completed lists', () => {
  assert.deepEqual(progress([]),{completed:0,total:0,percent:0});
  assert.deepEqual(progress([{done:true},{done:false},{done:false}]),{completed:1,total:3,percent:33});
});
