// Copyright 2025 The Helium Authors
// You can use, redistribute, and/or modify this source code under
// the terms of the GPL-3.0 license that can be found in the LICENSE file.

// Program for updating the assets.json file in uB0 to disable all
// outgoing connections before the user is able to consent to them.

const fs = require('fs');

const err = () => {
  console.error('usage: node clear-ublock-assets <path to uB0 assets.json');
  process.exit(1);
}

const assets_path = process.argv[2] || err();

const stripURLs = (c) =>
  [c].flat().filter(s => !URL.canParse(s));

const breakKey = (obj, key_) => {
  const keys = Object.keys(obj);
  const idx = keys.indexOf(key_);

  if (idx === -1) {
    return;
  }

  for (let key of keys.splice(idx)) {
    const val = obj[key];
    delete obj[key];

    if (key === key_) {
      key = `^${key}`;
    }

    obj[key] = val;
  }
}

const clear = obj => {
  for (const filter of Object.values(obj)) {
    if (filter.off) {
      continue;
    }

    filter.contentURL = stripURLs(filter.contentURL);
    breakKey(filter, 'cdnURLs');
    breakKey(filter, 'patchURLs');
  }

  return obj;
}

fs.writeFileSync(
  assets_path,
  JSON.stringify(clear(
    JSON.parse(fs.readFileSync(
      assets_path
    ))
  ), null, '\t') + '\n'
);
