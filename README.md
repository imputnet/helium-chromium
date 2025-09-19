# Helium
Bullshit-free web browser, based on Chromium. Follows [imput](https://github.com/imputnet)'s ethics and norms.

First and foremost, we're making a good browser for ourselves.
We don't intend to reinvent the wheel or target everyone, it isn't Helium's goal.
The main goal is to provide an honest, comfortable, privacy-respecting, and non-invasive experience.
If you don't like it - you don't like it, that's totally okay, and we don't care.

There's a lot more to Helium, but we don't have a complete set of features yet.
We'll update the documentation when we're closer to a public release!

## Platform-specific packaging
At the moment, only [Helium for macOS](https://github.com/imputnet/helium-macos) is polished and ready for daily use.

We also have packaging for Linux and Windows, but both of them are WIP:
- [Helium for Linux](https://github.com/imputnet/helium-linux) (AppImage)
- [Helium for Windows](https://github.com/imputnet/helium-windows) (no auto-updates yet)

## Credits
### ungoogled-chromium
Helium is proudly based on [ungoogled-chromium](https://github.com/ungoogled-software/ungoogled-chromium).
It wouldn't be possible for us to get rid of Google's bloat and get a development+building pipeline this fast without it.
Huge shout-out to everyone behind this amazing project!
(and we intend to contribute even more stuff upstream in the future)

### The Chromium project
[The Chromium Project](https://www.chromium.org/) is obviously at the core of Helium,
making it possible to exist in the first place.

### ungoogled-chromium's dependencies
- [Inox patchset](https://github.com/gcarq/inox-patchset)
- [Debian](https://tracker.debian.org/pkg/chromium-browser)
- [Bromite](https://github.com/bromite/bromite)
- [Iridium Browser](https://iridiumbrowser.de/)

## License
All code, patches, modified portions of imported code or patches, and
any other content that is unique to Helium and not imported from other
repositories is licensed under GPL-3.0. See [LICENSE](LICENSE).

Any content imported from other projects retains its original license (for
example, any original unmodified code imported from ungoogled-chromium remains
licensed under their [BSD 3-Clause license](LICENSE.ungoogled_chromium)).
