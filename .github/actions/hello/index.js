const core = require('@actions/core');

async function run() {
  core.info("Hello World from custom Action!");
  core.setOutput("msg", "👋 Olá do meu Hello World!");
}

run();