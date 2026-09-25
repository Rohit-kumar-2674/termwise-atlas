/* Shared pure chooser logic; route records come from data/routes.json. */
(function (root) {
  'use strict';
  function chooseRoute(data, platform, goal, ram) {
    if (!data.platforms.includes(platform) || !data.goals.includes(goal) || !data.ram_choices.includes(Number(ram))) {
      throw new Error('Choose a documented device, goal, and memory option.');
    }
    const result = data.routes.find(route => {
      const rule = route.when;
      return (!rule.platform || rule.platform.includes(platform)) &&
        (!rule.goal || rule.goal.includes(goal)) &&
        (rule.ram_max === undefined || Number(ram) <= rule.ram_max);
    });
    if (!result) throw new Error('Missing fallback route.');
    return result;
  }
  if (typeof module !== 'undefined' && module.exports) module.exports = { chooseRoute };
  else root.TermwiseRoutes = { chooseRoute };
})(typeof window !== 'undefined' ? window : globalThis);
