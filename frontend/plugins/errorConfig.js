/**
 * This file contains the errorcode configuration for the app.
 *
 * code: it is error code determined for this app.
 * Values start at 701 to avoid confusion with HTTP statusCodes.
 * Error capture in nuxt do not contains "statusError" property, only "message" property
 * This "message" property is not provided to user.
 *
 * msg: it is message provided when the error occures. The chain matches to chain used by i18n
 * (internationalization). Refer in '~/locales/*'.
 */
errorCodes = {
  // refer login-component (ID/Password error)
  authentication: {
    code: 401,
    msg: 'id-pwd-issue',
  },
  // refer login-component
  login: {
    code: 601,
    msg: 'login-issue',
  },
  // refer loadNomenclatures in nomenclatureStore
  nomenclature_not_found: {
    code: 701,
    msg: 'nomenclature_not_found_resource',
  },
  // refer loadNomenclatures in nomenclatureStore
  loading_whole_nomenclatures: {
    code: 702,
    msg: 'loading-issue',
  },
  // refer getConditions in nomenclatureStore
  get_infrstr_conditions: {
    code: 703,
    msg: 'loading-conditions-issue',
  },
  // refer getOwners in nomenclatureStore
  get_infrstr_owners: {
    code: 704,
    msg: 'loading-owners-issue',
  },
  // refer getPoleTypes in nomenclatureStore
  get_infrstr_poletypes: {
    code: 705,
    msg: 'loading-poletypes-issue',
  },
  // refer getPoleTypes in nomenclatureStore
  get_infrstr_risklevels: {
    code: 706,
    msg: 'loading-risklevels-issue',
  },
  // refer submit in point-component
  create_point: {
    code: 801,
    msg: 'create-issue',
  },
  // refer submit in line-component
  create_line: {
    code: 802,
    msg: 'create-issue',
  },
  // refer submit in point-component
  create_pole_diagnosis: {
    code: 803,
    msg: 'create-issue',
  },
  // refer submit in line-component
  create_line_diagnosis: {
    code: 804,
    msg: 'create-issue',
  },
  // refer loadImage in pictureComponent
  img_loading: {
    code: 901,
    msg: 'loading-img-issue',
  },
  // refer submit in related form component
  img_sending: {
    code: 902,
    msg: 'sending-img-issue',
  },
}
