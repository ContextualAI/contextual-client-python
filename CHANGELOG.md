# Changelog

## 0.9.1 (2025-10-31)

Full Changelog: [v0.9.0...v0.9.1](https://github.com/ContextualAI/contextual-client-python/compare/v0.9.0...v0.9.1)

### Bug Fixes

* **client:** close streams without requiring full consumption ([3f212eb](https://github.com/ContextualAI/contextual-client-python/commit/3f212ebb31085b404c72d827f1d6992dd4bed24c))


### Chores

* **internal/tests:** avoid race condition with implicit client cleanup ([f7f3568](https://github.com/ContextualAI/contextual-client-python/commit/f7f35681c6ac40661872fbdc3159e79ff764d135))

## 0.9.0 (2025-10-28)

Full Changelog: [v0.8.0...v0.9.0](https://github.com/ContextualAI/contextual-client-python/compare/v0.8.0...v0.9.0)

### Features

* **api:** update via SDK Studio ([3ebbcab](https://github.com/ContextualAI/contextual-client-python/commit/3ebbcab780e0391c420126b8cbf11589aba78470))
* improve future compat with pydantic v3 ([2837532](https://github.com/ContextualAI/contextual-client-python/commit/2837532cb8930994be7d02c356421a1a3e990c78))
* **types:** replace List[str] with SequenceNotStr in params ([ee66bc5](https://github.com/ContextualAI/contextual-client-python/commit/ee66bc5ce67fefb92b384ea979475ed54a53af9d))


### Bug Fixes

* avoid newer type syntax ([551b56e](https://github.com/ContextualAI/contextual-client-python/commit/551b56e22af03e8305e599814f484a5ed64b9cb3))
* **compat:** compat with `pydantic&lt;2.8.0` when using additional fields ([ceb597f](https://github.com/ContextualAI/contextual-client-python/commit/ceb597f1da87f0e2ae718a6143ec57c60b8f4d3d))


### Chores

* bump `httpx-aiohttp` version to 0.1.9 ([bdcc7c6](https://github.com/ContextualAI/contextual-client-python/commit/bdcc7c6b9c7784c25b49debbcadca2307c43e5b6))
* do not install brew dependencies in ./scripts/bootstrap by default ([41397b2](https://github.com/ContextualAI/contextual-client-python/commit/41397b25ce468bf58ed53e8e78e7cea2fcf41a47))
* **internal:** add Sequence related utils ([f00b892](https://github.com/ContextualAI/contextual-client-python/commit/f00b892536ef8c2d6f67965d7db28a1956adebb5))
* **internal:** detect missing future annotations with ruff ([6958d77](https://github.com/ContextualAI/contextual-client-python/commit/6958d772079b5f5571e7db3c39255d146b11dd5b))
* **internal:** improve examples ([c6f06b9](https://github.com/ContextualAI/contextual-client-python/commit/c6f06b9b0859a68bb32fa96294443abd139070e4))
* **internal:** move mypy configurations to `pyproject.toml` file ([57b4284](https://github.com/ContextualAI/contextual-client-python/commit/57b42849dd5340b2ce21aa8b6b8fb0c7e15529ba))
* **internal:** update pydantic dependency ([35223af](https://github.com/ContextualAI/contextual-client-python/commit/35223af9a91cc39d4800294b7821480ac2d2b0ee))
* **internal:** update pyright exclude list ([e89669e](https://github.com/ContextualAI/contextual-client-python/commit/e89669e93ed4a4e74993adfee5756b3502719e8c))
* **tests:** simplify `get_platform` test ([1f089bd](https://github.com/ContextualAI/contextual-client-python/commit/1f089bdf7319dee3c726d844d11f35a924cfdcc4))
* **types:** change optional parameter type from NotGiven to Omit ([07ee8a4](https://github.com/ContextualAI/contextual-client-python/commit/07ee8a4cecd02070a7fd44d1daec9687af2fce45))

## 0.8.0 (2025-08-26)

Full Changelog: [v0.7.0...v0.8.0](https://github.com/ContextualAI/contextual-client-python/compare/v0.7.0...v0.8.0)

### Features

* **api:** update via SDK Studio ([04fabfd](https://github.com/ContextualAI/contextual-client-python/commit/04fabfd2dd9bc21d5481bbea16148d9300e21196))
* **api:** update via SDK Studio ([feab9f8](https://github.com/ContextualAI/contextual-client-python/commit/feab9f82b627246dbc5592a7ba6bac5de7afd7e1))
* clean up environment call outs ([5aacfd7](https://github.com/ContextualAI/contextual-client-python/commit/5aacfd73cd62e9440b927c74e29bd4ee03766334))
* **client:** add follow_redirects request option ([35e7c78](https://github.com/ContextualAI/contextual-client-python/commit/35e7c78c7d1801a0afe4d73bbff3e7c695f5f19f))
* **client:** add support for aiohttp ([d54f53c](https://github.com/ContextualAI/contextual-client-python/commit/d54f53cfa0878acbad344622f7aae1b2e939ae1c))
* **client:** support file upload requests ([44d064d](https://github.com/ContextualAI/contextual-client-python/commit/44d064d3013ef31ec6cb709682ab5fef4d2ed531))


### Bug Fixes

* **ci:** correct conditional ([0e1ab57](https://github.com/ContextualAI/contextual-client-python/commit/0e1ab57132d5a038aac790b463166200ae436fc3))
* **ci:** release-doctor — report correct token name ([ce0af3b](https://github.com/ContextualAI/contextual-client-python/commit/ce0af3be8b2f90af2bc4e38979a801df1e98e989))
* **client:** correctly parse binary response | stream ([518cbab](https://github.com/ContextualAI/contextual-client-python/commit/518cbabda3ce7f53721c0fc916ae89706899a4ec))
* **client:** don't send Content-Type header on GET requests ([1ba6bcc](https://github.com/ContextualAI/contextual-client-python/commit/1ba6bcc49090112b3ec0dc9a0b1f5c2b487e378e))
* **docs/api:** remove references to nonexistent types ([9fd7133](https://github.com/ContextualAI/contextual-client-python/commit/9fd7133c6748ba1b1676a674da35d57f02f01a86))
* **parsing:** correctly handle nested discriminated unions ([130f4c1](https://github.com/ContextualAI/contextual-client-python/commit/130f4c17f8fbf89a42fa1709d6e4b4a8b36c4036))
* **parsing:** ignore empty metadata ([a81e190](https://github.com/ContextualAI/contextual-client-python/commit/a81e19084356382c7b709215b1462e099d56f2a6))
* **parsing:** parse extra field types ([89f10b3](https://github.com/ContextualAI/contextual-client-python/commit/89f10b3a97483b99e0ec06a346286619faec5c12))
* resolve pydantic violation. ([afcfc1c](https://github.com/ContextualAI/contextual-client-python/commit/afcfc1cb265aa3911164ea727af5de6d965d15a5))
* **tests:** fix: tests which call HTTP endpoints directly with the example parameters ([d7920f1](https://github.com/ContextualAI/contextual-client-python/commit/d7920f111d6175e6714482918e34992fb51739d9))


### Chores

* **ci:** change upload type ([f72dfb7](https://github.com/ContextualAI/contextual-client-python/commit/f72dfb77ff1fcae80efa5b286800ed77af6d0889))
* **ci:** enable for pull requests ([84fbba4](https://github.com/ContextualAI/contextual-client-python/commit/84fbba4c22dbbf8517841c7961a37dba246126dc))
* **ci:** fix installation instructions ([f191464](https://github.com/ContextualAI/contextual-client-python/commit/f191464e75f48395e76d6007712ae8548268b45f))
* **ci:** only run for pushes and fork pull requests ([b9520a0](https://github.com/ContextualAI/contextual-client-python/commit/b9520a0ad9c16d3ad0386ce70a15df4191751364))
* **ci:** upload sdks to package manager ([1f04b9e](https://github.com/ContextualAI/contextual-client-python/commit/1f04b9ecca3a4a3d2235c5cfa21bd9b36a358754))
* **docs:** grammar improvements ([01370fb](https://github.com/ContextualAI/contextual-client-python/commit/01370fb62278f1def879352910c2520102c89993))
* **docs:** remove reference to rye shell ([68f70a8](https://github.com/ContextualAI/contextual-client-python/commit/68f70a88e5b45773140c4b4a02c0506f3d078ad9))
* **docs:** remove unnecessary param examples ([f603dcd](https://github.com/ContextualAI/contextual-client-python/commit/f603dcdd966c77ce3e8b8dba8e878eb273ef1688))
* **internal:** bump pinned h11 dep ([f0aca79](https://github.com/ContextualAI/contextual-client-python/commit/f0aca79b109176c6a83b31434ccdbc30e58f059d))
* **internal:** change ci workflow machines ([9e79111](https://github.com/ContextualAI/contextual-client-python/commit/9e7911165b348e96ad55b6fd7faf8855c009c26f))
* **internal:** codegen related update ([0310d7c](https://github.com/ContextualAI/contextual-client-python/commit/0310d7ce2bca6a80cd3b0d53a1103b4dc1fa8c32))
* **internal:** fix ruff target version ([465af9e](https://github.com/ContextualAI/contextual-client-python/commit/465af9ec69d6456078fb4137b39d1dd33a3f60b2))
* **internal:** update comment in script ([01101c7](https://github.com/ContextualAI/contextual-client-python/commit/01101c7ff8496be98feb71c14eda4b6695cc7331))
* **internal:** update conftest.py ([b324ed3](https://github.com/ContextualAI/contextual-client-python/commit/b324ed373c9c174a44eb52dc6d2384e82c0af4b8))
* **internal:** update examples ([40379a3](https://github.com/ContextualAI/contextual-client-python/commit/40379a3d51aef12b1a0264e515ac145c91e41644))
* **package:** mark python 3.13 as supported ([f37217f](https://github.com/ContextualAI/contextual-client-python/commit/f37217ff20d84d47c9adaf89c14151075e329972))
* **project:** add settings file for vscode ([77265c1](https://github.com/ContextualAI/contextual-client-python/commit/77265c18261b46255146f4a0fd82e2aae41ae160))
* **readme:** fix version rendering on pypi ([5857ef3](https://github.com/ContextualAI/contextual-client-python/commit/5857ef3c8252e39ab66b1dea3e035580d0f2f006))
* **readme:** update badges ([b747f45](https://github.com/ContextualAI/contextual-client-python/commit/b747f452ab31df0805dd07a516fe63c460353c57))
* **tests:** add tests for httpx client instantiation & proxies ([0c4973f](https://github.com/ContextualAI/contextual-client-python/commit/0c4973fed123a77a16b189439b3f4976fcc91770))
* **tests:** run tests in parallel ([f75c912](https://github.com/ContextualAI/contextual-client-python/commit/f75c912ff643028317dde5fb0dfd08470b26ac29))
* **tests:** skip some failing tests on the latest python versions ([dd32830](https://github.com/ContextualAI/contextual-client-python/commit/dd32830a8266dbf736c85285ec611854659511e7))
* update @stainless-api/prism-cli to v5.15.0 ([82c8bc7](https://github.com/ContextualAI/contextual-client-python/commit/82c8bc7b281e624cff3606c46dea4a00ed99cc05))
* update github action ([2d36800](https://github.com/ContextualAI/contextual-client-python/commit/2d36800896a198d92225efa540eb4f0faff092aa))


### Documentation

* **client:** fix httpx.Timeout documentation reference ([3517a3d](https://github.com/ContextualAI/contextual-client-python/commit/3517a3d02c7447c027bc82baf3a83333eb3c9b55))

## 0.7.0 (2025-05-13)

Full Changelog: [v0.6.0...v0.7.0](https://github.com/ContextualAI/contextual-client-python/compare/v0.6.0...v0.7.0)

### Features

* **api:** update via SDK Studio ([656a0e1](https://github.com/ContextualAI/contextual-client-python/commit/656a0e19d78fe677a1a859bff114511acd58fa87))


### Bug Fixes

* **package:** support direct resource imports ([109de24](https://github.com/ContextualAI/contextual-client-python/commit/109de24d9c76aaa1d90fff8dfc816e5cfbfab50a))
* **tests:** correct number examples ([cb94e10](https://github.com/ContextualAI/contextual-client-python/commit/cb94e101a87b8abec57d46667fecef7a3079765f))


### Chores

* **internal:** avoid errors for isinstance checks on proxies ([581e581](https://github.com/ContextualAI/contextual-client-python/commit/581e581480ac98e0fed61eacc36e90a44e3b99fc))

## 0.6.0 (2025-05-08)

Full Changelog: [v0.5.1...v0.6.0](https://github.com/ContextualAI/contextual-client-python/compare/v0.5.1...v0.6.0)

### Features

* **api:** update via SDK Studio ([2024a46](https://github.com/ContextualAI/contextual-client-python/commit/2024a46629ceca81d6c146b2e4d92ed4afb72e4b))
* **api:** update via SDK Studio ([dba986f](https://github.com/ContextualAI/contextual-client-python/commit/dba986f3194a37160064270836d15a88ed0f8ee4))
* **api:** update via SDK Studio ([a707edc](https://github.com/ContextualAI/contextual-client-python/commit/a707edc06c74353788bfa182d07682f7352a7a02))
* **api:** update via SDK Studio ([#68](https://github.com/ContextualAI/contextual-client-python/issues/68)) ([7b8f948](https://github.com/ContextualAI/contextual-client-python/commit/7b8f9488ff9ba324210a23694065830a25985edc))
* **api:** update via SDK Studio ([#70](https://github.com/ContextualAI/contextual-client-python/issues/70)) ([25477c7](https://github.com/ContextualAI/contextual-client-python/commit/25477c7d93934f2b5b72f5b24857f023c17349cf))
* **api:** update via SDK Studio ([#73](https://github.com/ContextualAI/contextual-client-python/issues/73)) ([e07435e](https://github.com/ContextualAI/contextual-client-python/commit/e07435e7ab08a53cd13f4f8d91f2baca1ec2c28d))


### Bug Fixes

* **ci:** ensure pip is always available ([#79](https://github.com/ContextualAI/contextual-client-python/issues/79)) ([ec1e2ce](https://github.com/ContextualAI/contextual-client-python/commit/ec1e2ce6de25021983b0a48b90069f24e3ee8def))
* **ci:** remove publishing patch ([#80](https://github.com/ContextualAI/contextual-client-python/issues/80)) ([9e32578](https://github.com/ContextualAI/contextual-client-python/commit/9e32578922eb4dbad057231999add02c8aca3eb1))
* **perf:** optimize some hot paths ([b88026d](https://github.com/ContextualAI/contextual-client-python/commit/b88026d6bfee7100a5663a95dd9800ed0059b353))
* **perf:** skip traversing types for NotGiven values ([5bd2eab](https://github.com/ContextualAI/contextual-client-python/commit/5bd2eabd88852941a46d70823cb6163db08558eb))
* **pydantic v1:** more robust ModelField.annotation check ([ce1ecab](https://github.com/ContextualAI/contextual-client-python/commit/ce1ecab62f47913665a51e3116232f65de95a3f3))
* testing value for tune endpoints. ([7be555f](https://github.com/ContextualAI/contextual-client-python/commit/7be555fe0f39430923a9473420a88fc8c065a299))
* **types:** handle more discriminated union shapes ([#78](https://github.com/ContextualAI/contextual-client-python/issues/78)) ([473adf4](https://github.com/ContextualAI/contextual-client-python/commit/473adf4d731241a2c34271d39a37d0ac2bc99d4e))


### Chores

* broadly detect json family of content-type headers ([f4f3951](https://github.com/ContextualAI/contextual-client-python/commit/f4f39513b3f9a1c1cb5f323d2c0da2b0d04eff06))
* **ci:** add timeout thresholds for CI jobs ([542b4ad](https://github.com/ContextualAI/contextual-client-python/commit/542b4adaefef61d93d6d7ec971c50d3d87490c17))
* **ci:** only use depot for staging repos ([973153b](https://github.com/ContextualAI/contextual-client-python/commit/973153b08c9780b0d27ee107f71045c5921ee4f5))
* **client:** minor internal fixes ([379b18e](https://github.com/ContextualAI/contextual-client-python/commit/379b18e3382f4cb3cbf2f4fb768a0d23885ec562))
* fix typos ([#81](https://github.com/ContextualAI/contextual-client-python/issues/81)) ([9ba43be](https://github.com/ContextualAI/contextual-client-python/commit/9ba43bed2b39d60d599b90e624a2a40e57584749))
* **internal:** base client updates ([1c44fea](https://github.com/ContextualAI/contextual-client-python/commit/1c44fea55a67de0d11f00fd3b63f64302f5eee51))
* **internal:** bump pyright version ([6878eae](https://github.com/ContextualAI/contextual-client-python/commit/6878eae3717d1076836f59dafcab08a44ec573c8))
* **internal:** bump rye to 0.44.0 ([#77](https://github.com/ContextualAI/contextual-client-python/issues/77)) ([520ba3a](https://github.com/ContextualAI/contextual-client-python/commit/520ba3a8e069a19543238009a241579ede90c2fe))
* **internal:** codegen related update ([ddb9f6c](https://github.com/ContextualAI/contextual-client-python/commit/ddb9f6c3be981908de24cb485b4787a2fa969b80))
* **internal:** codegen related update ([#74](https://github.com/ContextualAI/contextual-client-python/issues/74)) ([6e8bc46](https://github.com/ContextualAI/contextual-client-python/commit/6e8bc46fab20d9babe7b047298b55b0565ba4a8b))
* **internal:** expand CI branch coverage ([fce3ddf](https://github.com/ContextualAI/contextual-client-python/commit/fce3ddf98a13402dc63da54b1042e625247e1e72))
* **internal:** fix list file params ([561214d](https://github.com/ContextualAI/contextual-client-python/commit/561214d491c29833c6babc1ad1f5d6cc4367f794))
* **internal:** import reformatting ([a9e8ae2](https://github.com/ContextualAI/contextual-client-python/commit/a9e8ae26c8f15d4bc385890eb0954d41475f5fba))
* **internal:** minor formatting changes ([d036bee](https://github.com/ContextualAI/contextual-client-python/commit/d036bee6b1e9e9bf16d775f1f48732d5cf0bd206))
* **internal:** reduce CI branch coverage ([b10d32e](https://github.com/ContextualAI/contextual-client-python/commit/b10d32ecd725652eba23d9e14714f82af0ead691))
* **internal:** refactor retries to not use recursion ([7689427](https://github.com/ContextualAI/contextual-client-python/commit/7689427fe4667c1efcf66ba7ee6ace7e2dbd05f3))
* **internal:** remove extra empty newlines ([#75](https://github.com/ContextualAI/contextual-client-python/issues/75)) ([8117197](https://github.com/ContextualAI/contextual-client-python/commit/81171975661f4a03f22820a36773bdff14b79e20))
* **internal:** remove trailing character ([#82](https://github.com/ContextualAI/contextual-client-python/issues/82)) ([72018c8](https://github.com/ContextualAI/contextual-client-python/commit/72018c8784cf5d9974fca682b2b9998e2c4d341c))
* **internal:** slight transform perf improvement ([#83](https://github.com/ContextualAI/contextual-client-python/issues/83)) ([29e9d80](https://github.com/ContextualAI/contextual-client-python/commit/29e9d80b25a84deb927098fd9c7bc0341a8e165f))
* **internal:** update models test ([c3fcd9c](https://github.com/ContextualAI/contextual-client-python/commit/c3fcd9c8c1ef3de1b9681a8298ac508b758bf98c))
* **internal:** update pyright settings ([9a560f4](https://github.com/ContextualAI/contextual-client-python/commit/9a560f4f6234c724a0426356e1c154ddfbccfa71))
* slight wording improvement in README ([#84](https://github.com/ContextualAI/contextual-client-python/issues/84)) ([d5d7f2a](https://github.com/ContextualAI/contextual-client-python/commit/d5d7f2a5ece5735e83e431c9f231b94eb7d41773))
* use lazy imports for resources ([e41fd1c](https://github.com/ContextualAI/contextual-client-python/commit/e41fd1c3869c16d18ba7f9151a1b3f1a463f0fd6))

## 0.5.1 (2025-03-11)

Full Changelog: [v0.5.0...v0.5.1](https://github.com/ContextualAI/contextual-client-python/compare/v0.5.0...v0.5.1)

### Features

* **api:** update via SDK Studio ([#65](https://github.com/ContextualAI/contextual-client-python/issues/65)) ([b890fa1](https://github.com/ContextualAI/contextual-client-python/commit/b890fa187655a83f4d5251916ba887e91dc0193e))

## 0.5.0 (2025-03-11)

Full Changelog: [v0.4.0...v0.5.0](https://github.com/ContextualAI/contextual-client-python/compare/v0.4.0...v0.5.0)

### Features

* Add to_dataframe method to BinaryAPIReponse ([#56](https://github.com/ContextualAI/contextual-client-python/issues/56)) ([39b862e](https://github.com/ContextualAI/contextual-client-python/commit/39b862eca8d7443c2c86063123d8dfdc484a3c53))
* **api:** update via SDK Studio ([#63](https://github.com/ContextualAI/contextual-client-python/issues/63)) ([59bb1ab](https://github.com/ContextualAI/contextual-client-python/commit/59bb1ab3d790ee7e3d73b2b6a85e67a905d0ca22))


### Chores

* **internal:** remove unused http client options forwarding ([#61](https://github.com/ContextualAI/contextual-client-python/issues/61)) ([40d345d](https://github.com/ContextualAI/contextual-client-python/commit/40d345dd52af82e31e8fa34e5b0b1eebad006684))

## 0.4.0 (2025-03-03)

Full Changelog: [v0.3.0...v0.4.0](https://github.com/ContextualAI/contextual-client-python/compare/v0.3.0...v0.4.0)

### Features

* Add special snowflake path for internal dns usage ([#52](https://github.com/ContextualAI/contextual-client-python/issues/52)) ([dd0ea41](https://github.com/ContextualAI/contextual-client-python/commit/dd0ea4117c37eb53620304a30f736747f30f6ce6))
* **api:** update via SDK Studio ([#59](https://github.com/ContextualAI/contextual-client-python/issues/59)) ([9b116a4](https://github.com/ContextualAI/contextual-client-python/commit/9b116a4e1d935a32ab8a44a36042891edf4d2125))


### Chores

* **docs:** update client docstring ([#55](https://github.com/ContextualAI/contextual-client-python/issues/55)) ([ef1ee6e](https://github.com/ContextualAI/contextual-client-python/commit/ef1ee6e351e2c1a84af871f70742045df23fbe7f))


### Documentation

* update URLs from stainlessapi.com to stainless.com ([#53](https://github.com/ContextualAI/contextual-client-python/issues/53)) ([4162888](https://github.com/ContextualAI/contextual-client-python/commit/41628880bfb7d72cb3759ea06f1c09c11bb60e1a))

## 0.3.0 (2025-02-26)

Full Changelog: [v0.2.0...v0.3.0](https://github.com/ContextualAI/contextual-client-python/compare/v0.2.0...v0.3.0)

### Features

* **api:** update via SDK Studio ([#41](https://github.com/ContextualAI/contextual-client-python/issues/41)) ([4b3ea42](https://github.com/ContextualAI/contextual-client-python/commit/4b3ea42dd9effb3cec4fb078800ca96dc3609617))
* **api:** update via SDK Studio ([#49](https://github.com/ContextualAI/contextual-client-python/issues/49)) ([d54defd](https://github.com/ContextualAI/contextual-client-python/commit/d54defd3a23a488c24cae38bedd86d5721d8a71b))
* **api:** update via SDK Studio ([#50](https://github.com/ContextualAI/contextual-client-python/issues/50)) ([6060be1](https://github.com/ContextualAI/contextual-client-python/commit/6060be19c881d87e5ab7b63bc60f536a6b9e70cc))
* **client:** allow passing `NotGiven` for body ([#46](https://github.com/ContextualAI/contextual-client-python/issues/46)) ([4e2264d](https://github.com/ContextualAI/contextual-client-python/commit/4e2264da0b35d4dcfbf33a77950f0f7d57f1db14))


### Bug Fixes

* asyncify on non-asyncio runtimes ([#44](https://github.com/ContextualAI/contextual-client-python/issues/44)) ([3a16763](https://github.com/ContextualAI/contextual-client-python/commit/3a16763381747ee6ccf829fb535927446634d54c))
* **client:** mark some request bodies as optional ([4e2264d](https://github.com/ContextualAI/contextual-client-python/commit/4e2264da0b35d4dcfbf33a77950f0f7d57f1db14))


### Chores

* **internal:** codegen related update ([#45](https://github.com/ContextualAI/contextual-client-python/issues/45)) ([2651383](https://github.com/ContextualAI/contextual-client-python/commit/26513832dc75629f229493f4718e97a34588fd97))
* **internal:** fix devcontainers setup ([#47](https://github.com/ContextualAI/contextual-client-python/issues/47)) ([f5ea511](https://github.com/ContextualAI/contextual-client-python/commit/f5ea51125d954e2ef39e817c0a7bae763661c571))
* **internal:** properly set __pydantic_private__ ([#48](https://github.com/ContextualAI/contextual-client-python/issues/48)) ([b49c8a0](https://github.com/ContextualAI/contextual-client-python/commit/b49c8a0b97a15495912999b97b6b754d2dcfbb4e))
* **internal:** update client tests ([#43](https://github.com/ContextualAI/contextual-client-python/issues/43)) ([ee164e9](https://github.com/ContextualAI/contextual-client-python/commit/ee164e9e3a7f15570560922d383565ea4a50d446))

## 0.2.0 (2025-02-08)

Full Changelog: [v0.1.0...v0.2.0](https://github.com/ContextualAI/contextual-client-python/compare/v0.1.0...v0.2.0)

### Features

* **api:** update via SDK Studio ([#31](https://github.com/ContextualAI/contextual-client-python/issues/31)) ([c9de385](https://github.com/ContextualAI/contextual-client-python/commit/c9de38561c8663d1e00daa381fcb3183501993cf))
* **api:** update via SDK Studio ([#32](https://github.com/ContextualAI/contextual-client-python/issues/32)) ([c166d77](https://github.com/ContextualAI/contextual-client-python/commit/c166d77d241e104a80ce0cddeaf2b5cfe7c59669))
* **api:** update via SDK Studio ([#39](https://github.com/ContextualAI/contextual-client-python/issues/39)) ([9f8c0a6](https://github.com/ContextualAI/contextual-client-python/commit/9f8c0a6d4203953f195cfe5d38a69f8870bc0a9e))
* **client:** send `X-Stainless-Read-Timeout` header ([#35](https://github.com/ContextualAI/contextual-client-python/issues/35)) ([2ddba9d](https://github.com/ContextualAI/contextual-client-python/commit/2ddba9dc9d8cb0b562c6dd7f8a3a21e2c82295bc))


### Bug Fixes

* **tests:** make test_get_platform less flaky ([#26](https://github.com/ContextualAI/contextual-client-python/issues/26)) ([3bc8a69](https://github.com/ContextualAI/contextual-client-python/commit/3bc8a69c6e9255dc1e3247fd1954e5deb5e1c155))


### Chores

* **internal:** avoid pytest-asyncio deprecation warning ([#27](https://github.com/ContextualAI/contextual-client-python/issues/27)) ([e6f70cd](https://github.com/ContextualAI/contextual-client-python/commit/e6f70cdff84defcb3b9d77e3aa0c66e9d17774d5))
* **internal:** bummp ruff dependency ([#34](https://github.com/ContextualAI/contextual-client-python/issues/34)) ([f3a23c2](https://github.com/ContextualAI/contextual-client-python/commit/f3a23c21168a5ef99626e50782ae902c780b4059))
* **internal:** change default timeout to an int ([#33](https://github.com/ContextualAI/contextual-client-python/issues/33)) ([280fc1f](https://github.com/ContextualAI/contextual-client-python/commit/280fc1fcce2a011bda2b895b39b85db682cc0c8c))
* **internal:** codegen related update ([#23](https://github.com/ContextualAI/contextual-client-python/issues/23)) ([d1f86c3](https://github.com/ContextualAI/contextual-client-python/commit/d1f86c3bc54440925725dd9c535082fa7d29d100))
* **internal:** codegen related update ([#30](https://github.com/ContextualAI/contextual-client-python/issues/30)) ([0cbc82e](https://github.com/ContextualAI/contextual-client-python/commit/0cbc82e361567e9f0c44f9b5519d404fcba91fef))
* **internal:** fix type traversing dictionary params ([#36](https://github.com/ContextualAI/contextual-client-python/issues/36)) ([04a1eab](https://github.com/ContextualAI/contextual-client-python/commit/04a1eaba9f246089baa2c26dac29b22e9f63f9dc))
* **internal:** minor formatting changes ([#29](https://github.com/ContextualAI/contextual-client-python/issues/29)) ([9d063fb](https://github.com/ContextualAI/contextual-client-python/commit/9d063fbf86e64803fcc684305a67dae3a31775a0))
* **internal:** minor style changes ([#28](https://github.com/ContextualAI/contextual-client-python/issues/28)) ([1cbda0a](https://github.com/ContextualAI/contextual-client-python/commit/1cbda0a834e06cbb4afdbc922e4e9f894cb21d40))
* **internal:** minor type handling changes ([#37](https://github.com/ContextualAI/contextual-client-python/issues/37)) ([dd9a8e8](https://github.com/ContextualAI/contextual-client-python/commit/dd9a8e898c56fc55b9e61de09419a66ad398b7b3))


### Documentation

* **raw responses:** fix duplicate `the` ([#25](https://github.com/ContextualAI/contextual-client-python/issues/25)) ([5342fdf](https://github.com/ContextualAI/contextual-client-python/commit/5342fdfbecdd99f14d0033736ebf91700bc74f0e))

## 0.1.0 (2025-01-15)

Full Changelog: [v0.1.0-alpha.2...v0.1.0](https://github.com/ContextualAI/contextual-client-python/compare/v0.1.0-alpha.2...v0.1.0)

### Features

* stable release. ([0a95ded](https://github.com/ContextualAI/contextual-client-python/commit/0a95dedf99d1252be7fd94a6ceafc751e1b04eee))

## 0.1.0-alpha.2 (2025-01-15)

Full Changelog: [v0.1.0-alpha.1...v0.1.0-alpha.2](https://github.com/ContextualAI/contextual-client-python/compare/v0.1.0-alpha.1...v0.1.0-alpha.2)

### Features

* **api:** update via SDK Studio ([#16](https://github.com/ContextualAI/contextual-client-python/issues/16)) ([eef8a87](https://github.com/ContextualAI/contextual-client-python/commit/eef8a87c1f4d1c57fce697103d07c8510fcc4520))
* **api:** update via SDK Studio ([#18](https://github.com/ContextualAI/contextual-client-python/issues/18)) ([990c359](https://github.com/ContextualAI/contextual-client-python/commit/990c359ab3f2e6c3f29fc07e158c895159e8cc94))
* **api:** update via SDK Studio ([#19](https://github.com/ContextualAI/contextual-client-python/issues/19)) ([4eeaea9](https://github.com/ContextualAI/contextual-client-python/commit/4eeaea95542c416d4dfa0d00e0304c3f88c2be79))

## 0.1.0-alpha.1 (2025-01-15)

Full Changelog: [v0.0.1-alpha.0...v0.1.0-alpha.1](https://github.com/ContextualAI/contextual-client-python/compare/v0.0.1-alpha.0...v0.1.0-alpha.1)

### Features

* **api:** update via SDK Studio ([b26af54](https://github.com/ContextualAI/contextual-client-python/commit/b26af545d014d2ebbb0b95786325776a76cf4c37))
* **api:** update via SDK Studio ([993c748](https://github.com/ContextualAI/contextual-client-python/commit/993c74879dc993e1c28f044fd7246bbd09d79a66))
* **api:** update via SDK Studio ([ed4eda6](https://github.com/ContextualAI/contextual-client-python/commit/ed4eda61c3aa6535e6252a69c3a324d5ae996ef7))
* **api:** update via SDK Studio ([89997a9](https://github.com/ContextualAI/contextual-client-python/commit/89997a98ea2019a768dde3d93f101871311185e0))
* **api:** update via SDK Studio ([c4f9a7a](https://github.com/ContextualAI/contextual-client-python/commit/c4f9a7ad111def98c39764d1c4af7c37f4704912))
* **api:** update via SDK Studio ([8ee9b9b](https://github.com/ContextualAI/contextual-client-python/commit/8ee9b9b7fa9ecb74097893b59b670675c399489d))
* **api:** update via SDK Studio ([a116bc0](https://github.com/ContextualAI/contextual-client-python/commit/a116bc03080ff09e0269c995c8e67dc49a8c563f))
* **api:** update via SDK Studio ([ef744ef](https://github.com/ContextualAI/contextual-client-python/commit/ef744ef0f11559c6df063fd68268be0ed646606b))
* **api:** update via SDK Studio ([04d45a7](https://github.com/ContextualAI/contextual-client-python/commit/04d45a7d0d6dddd8b826592146e696264975db37))
* **api:** update via SDK Studio ([5e4dab5](https://github.com/ContextualAI/contextual-client-python/commit/5e4dab55c8763098e750fe58f8501b1e21b08d11))
* **api:** update via SDK Studio ([18443a5](https://github.com/ContextualAI/contextual-client-python/commit/18443a52b8fe05eba8098295cd39f99d36de2d0e))
* **api:** update via SDK Studio ([17ba526](https://github.com/ContextualAI/contextual-client-python/commit/17ba5269a45738e5d7e0a833b887f32465266531))
* **api:** update via SDK Studio ([581ec7e](https://github.com/ContextualAI/contextual-client-python/commit/581ec7e0f55ad14aa72de15bae22d298b25df17d))
* **api:** update via SDK Studio ([9862571](https://github.com/ContextualAI/contextual-client-python/commit/986257157c57188953637bd4b43150a0492babcc))
* **api:** update via SDK Studio ([dedbd4a](https://github.com/ContextualAI/contextual-client-python/commit/dedbd4ad104e03310190ad0776ba959758365c87))
* **api:** update via SDK Studio ([a8bd7a6](https://github.com/ContextualAI/contextual-client-python/commit/a8bd7a6c3b40f03c6732fc5984dd82dd762a371b))
* **api:** update via SDK Studio ([eb46df2](https://github.com/ContextualAI/contextual-client-python/commit/eb46df2656bb40a05d5443f148529b2945cba2e6))
* **api:** update via SDK Studio ([d72e3cf](https://github.com/ContextualAI/contextual-client-python/commit/d72e3cfee20d002616d1f17412e919495b051e79))
* **api:** update via SDK Studio ([3d1cde0](https://github.com/ContextualAI/contextual-client-python/commit/3d1cde029bf1c7de64d82a18ce4a87097c0065c0))
* **api:** update via SDK Studio ([6cb72bf](https://github.com/ContextualAI/contextual-client-python/commit/6cb72bf6f0b8e4f14c15e4a8c6eac91dffce3358))
* **api:** update via SDK Studio ([73639c4](https://github.com/ContextualAI/contextual-client-python/commit/73639c4a11978159b2a1fbf7b5d849a6358852dc))
* **api:** update via SDK Studio ([3c4ff11](https://github.com/ContextualAI/contextual-client-python/commit/3c4ff11698404e2e391a8194b58a147b5b2a373a))
* use customized prism-cli from npm. ([86d8b36](https://github.com/ContextualAI/contextual-client-python/commit/86d8b36c7d99031057b5d16ad77d0fa3f54b0861))


### Bug Fixes

* **client:** only call .close() when needed ([e9f24af](https://github.com/ContextualAI/contextual-client-python/commit/e9f24af4d134d7919fde20dde45c928e8dc14680))
* correctly handle deserialising `cls` fields ([9b002bf](https://github.com/ContextualAI/contextual-client-python/commit/9b002bf0ec2bc6ea8fd79bef8eafddfa07f1fe3a))


### Chores

* add missing isclass check ([d373c16](https://github.com/ContextualAI/contextual-client-python/commit/d373c16e7e1d6964e603511a344c538afbd1b5c4))
* add universal flag to lock files. ([c745c46](https://github.com/ContextualAI/contextual-client-python/commit/c745c46eb528a52fc3c174ce91ca93177db533f8))
* code cleanup. ([b2d17e0](https://github.com/ContextualAI/contextual-client-python/commit/b2d17e02b6a0631da4bd067a7bba24f23871fa9f))
* ignore `.DS_Store`. ([4d88206](https://github.com/ContextualAI/contextual-client-python/commit/4d882066acf442591667f2b7bdc2412abff4a504))
* **internal:** add support for TypeAliasType ([8954c97](https://github.com/ContextualAI/contextual-client-python/commit/8954c972f145f840a75fda49e0fd842d2dcce024))
* **internal:** bump httpx dependency ([a1caab0](https://github.com/ContextualAI/contextual-client-python/commit/a1caab00b5bad0092c0d762395f5ddbf534957ea))
* **internal:** bump pydantic dependency ([f7caf20](https://github.com/ContextualAI/contextual-client-python/commit/f7caf20d9ce678e26a23f926e87d67b740f1a8f7))
* **internal:** bump pyright ([e78ad59](https://github.com/ContextualAI/contextual-client-python/commit/e78ad59a3d6cb212d3ff41d03469745c2fcaa3ad))
* **internal:** codegen related update ([6208f37](https://github.com/ContextualAI/contextual-client-python/commit/6208f37ebeda115283e07d7b497291bb105ae822))
* **internal:** codegen related update ([2c55602](https://github.com/ContextualAI/contextual-client-python/commit/2c556026684cc39ea763c67a26f3860529246f88))
* **internal:** codegen related update ([c90698a](https://github.com/ContextualAI/contextual-client-python/commit/c90698a2e6c51f1524c6f34cf599164309141eec))
* **internal:** codegen related update ([215c573](https://github.com/ContextualAI/contextual-client-python/commit/215c573ac64e31481c41f2635e908197b32da724))
* **internal:** codegen related update ([e943905](https://github.com/ContextualAI/contextual-client-python/commit/e9439056db5b3753011ecd1a2c944588e8405fbd))
* **internal:** fix some typos ([beafdbd](https://github.com/ContextualAI/contextual-client-python/commit/beafdbdd47fd466c76130dc1f72e7829edd76f39))
* remove custom code ([6ad0c2c](https://github.com/ContextualAI/contextual-client-python/commit/6ad0c2c8cbc8cbfa00fd961ac7053ce7232ed8df))
* update README. ([6b324de](https://github.com/ContextualAI/contextual-client-python/commit/6b324de7f2818bd3b6aa1d9e20ab47d3d74e25ea))


### Documentation

* fix typos ([ff04307](https://github.com/ContextualAI/contextual-client-python/commit/ff04307fb89c7da8ef313ee19e20ed19cad01f0c))
* **readme:** example snippet for client context manager ([fd9d286](https://github.com/ContextualAI/contextual-client-python/commit/fd9d2869b622ea1633b4ffd013d0ce2d090d03c8))
* **readme:** fix http client proxies example ([cca1f66](https://github.com/ContextualAI/contextual-client-python/commit/cca1f6666835843fbb560124667371f938d4e499))
