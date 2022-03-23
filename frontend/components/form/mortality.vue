<template>
  <v-card elevation="0" class="fill-height">
    <v-form ref="form" v-model="formValid" class="text-center">
      <v-toolbar color="pink" dark elevation="0">
        <v-toolbar-title>{{ $t('mortality.new_mortality') }}</v-toolbar-title>

        <v-spacer></v-spacer>

        <v-btn icon @click="$router.back()">
          <v-icon>mdi-close</v-icon>
        </v-btn>
      </v-toolbar>
      <v-card-text class="overflow-auto">
        <v-container>
          <v-row>
            <v-col cols="12" class="text-left">
              <strong>{{ $t('forms.coordinates') }}</strong>
            </v-col>
          </v-row>
          <v-row>
            <v-col cols="12" md="4">
              <v-text-field
                ref="lat"
                v-model="lat"
                :label="$t('support.latitude')"
                type="number"
                placeholder="Latitude"
                :rules="[rules.requiredOrNotValid, rules.latRange]"
                required
                hide-spin-buttons
                outlined
                dense
              />
              <!-- <v-text-field
                ref="lat"
                v-model="lat"
                :label="$t('support.latitude')"
                :disabled="!manualChange"
                type="number"
                placeholder="Latitude"
                :rules="[rules.requiredOrNotValid, rules.latRange]"
                required
                hide-spin-buttons
                outlined
                dense
              /> -->
            </v-col>

            <v-col cols="12" md="4">
              <v-text-field
                ref="lng"
                v-model="lng"
                :label="$t('support.longitude')"
                type="number"
                :rules="[rules.requiredOrNotValid, rules.lngRange]"
                required
                hide-spin-buttons
                outlined
                dense
              />
              <!-- <v-text-field
                ref="lng"
                v-model="lng"
                :label="$t('support.longitude')"
                :disabled="!manualChange"
                type="number"
                :rules="[rules.requiredOrNotValid, rules.lngRange]"
                required
                hide-spin-buttons
                outlined
                dense
              /> -->
            </v-col>

            <!-- <v-col cols="12" md="4">
              <v-checkbox
                v-model="manualChange"
                dense
                :label="$t('support.manual-handling')"
              ></v-checkbox>
            </v-col> -->
          </v-row>
        </v-container>
        <v-divider></v-divider>
        <v-container>
          <v-row>
            <v-col cols="12" class="text-left">
              <strong>{{ $t('forms.general') }}</strong>
            </v-col>
          </v-row>
          <v-row>
            <v-col cols="12" md="6">
              <v-menu
                :close-on-content-click="false"
                transition="scale-transition"
              >
                <template #activator="{ on, attrs }">
                  <v-text-field
                    v-model="mortalityData.date"
                    :label="$t('forms.datecreate')"
                    persistent-hint
                    prepend-icon="mdi-calendar"
                    readonly
                    outlined
                    dense
                    v-bind="attrs"
                    v-on="on"
                  ></v-text-field>
                </template>
                <v-date-picker
                  v-model="mortalityData.date"
                  no-title
                ></v-date-picker>
              </v-menu>
            </v-col>

            <v-col cols="12" md="6">
              <v-autocomplete
                v-model="mortalityData.species"
                :items="species"
                item-text="vernacular_name"
                item-value="id"
                :rules="[rules.required]"
                hide-selected
                label="Espèce"
                outlined
                dense
              ></v-autocomplete>
            </v-col>
            <v-col cols="12" md="6">
              <v-text-field
                ref="lat"
                v-model="mortalityData.author"
                :label="$t('mortality.observer')"
                type="string"
                :placeholder="$t('mortality.observer')"
                hide-spin-buttons
                outlined
                dense
              />
            </v-col>

            <v-col cols="12" md="6">
              <v-text-field
                ref="lat"
                v-model="mortalityData.infrstr"
                label="support/ligne concerné"
                type="string"
                placeholder="support/ligne concerné"
                hide-spin-buttons
                outlined
                dense
              />
            </v-col>

            <v-col cols="12">
              <v-textarea
                v-model="mortalityData.remark"
                clearable
                clear-icon="mdi-close-circle"
                :label="$t('app.remark')"
                :rules="[rules.textLength]"
                rows="2"
                counter="300"
                outlined
                dense
              ></v-textarea>
            </v-col>
          </v-row>
        </v-container>

        <v-divider></v-divider>
        <v-container>
          <v-row>
            <v-col cols="12" class="text-left">
              <strong>{{ $t('picture.pictures') }}</strong>
            </v-col>
          </v-row>
          <v-row>
            <v-col cols="12">
              <utils-picture-component ref="upc" />
            </v-col>
          </v-row>
        </v-container>
      </v-card-text>
      <v-card-actions>
        <v-row class="justify-space-around mb-2">
          <v-btn @click="back">{{ $t('app.cancel') }}</v-btn>
          <v-btn @click="submit">{{ $t('app.valid') }}</v-btn>
        </v-row>
      </v-card-actions>
    </v-form>
  </v-card>
</template>
<script>
import { mapGetters } from 'vuex'
import * as errorCodes from '~/static/errorConfig.json'

// export default Vue.extend({
export default {
  name: 'PointComponent',

  props: {
    mortality: { type: Object, default: null },
  },

  data() {
    return {
      formValid: true,
      // manualChange: false, // boolean to activate manual coordinate change
      // form values
      newLat: null,
      newLng: null,
      // define data related to Point
      pointData: {
        geom: {
          type: 'Point',
          coordinates: [],
        },
        owner_id: 1, // null,
      },
      // define data related to Diagnosis
      mortalityData: {
        date: new Date(Date.now() - new Date().getTimezoneOffset() * 60000)
          .toISOString()
          .substr(0, 10),
        author: null,
        species: null, // null,
        infrstr: null,
        nb_death: 0, // null,
        death_cause: null,
        data_source: null,
      },
      // rules for form validation
      rules: {
        required: (v) => !!v || this.$t('valid.required'),
        requiredOrNotValid: (v) =>
          !!v || this.$t('valid.required_or_not_valid'),
        latRange: (v) =>
          (v >= 40 && v <= 52) || `${this.$t('valid.range')}40 : 52`,
        lngRange: (v) =>
          (v >= -20 && v <= 20) || `${this.$t('valid.range')}-20 : 20`,
        textLength: (v) =>
          (v || '').length <= 300 || `${this.$t('valid.length')}: 300`,
      },
    }
  },
  computed: {
    /**
     * Getter and Setter for "lat" value.
     * This latitude value is bind v-text-field "lat", and linked with latitude of the LMarker
     * from map-component.
     * When value is commited, it is detected by map-component.vue
     */
    lat: {
      get() {
        return this.newPoint ? this.newPoint.lat : null // avoid bug if newPoint undefined
      },
      // on change in v-text-field, value is set to store.
      set(newVal) {
        this.$store.commit('coordinatesStore/addPointCoord', {
          lat: newVal !== '' ? Number(newVal) : null, // prevent Number('') returns 0
          lng: this.lng,
        })
      },
    },
    /**
     * Getter and Setter for "lng" value.
     * This longitude value is bind v-text-field "lng", and linked with longitude of the LMarker
     * from map-component.
     * When value is commited, it is detected by map-component.vue
     */
    lng: {
      get() {
        return this.newPoint ? this.newPoint.lng : null // avoid bug if newPoint undefined
      },
      // on change in v-text-field, value is set to store.
      set(newVal) {
        this.$store.commit('coordinatesStore/addPointCoord', {
          lat: this.lat,
          lng: newVal !== '' ? Number(newVal) : null, // prevent Number('') returns 0
        })
      },
    },
    // Get values from store
    ...mapGetters({
      newPoint: 'coordinatesStore/newPointCoord',
      species: 'speciesStore/getSpecies',
      riskLevels: 'nomenclaturesStore/getRiskLevels',
    }),
  },
  mounted() {
    this.$store.dispatch('speciesStore/loadSpecies')
  },
  methods: {
    /**
     * back(): Method to get back if cancel Point creation.
     *
     * "newPointCoord" reinitialized with lat and lng set to null
     */
    back() {
      this.$store.commit('coordinatesStore/addPointCoord', {
        lat: null,
        lng: null,
      })
      this.$router.back()
    },

    /**
     * submit(): Method to submit the form for Point/Diagnosis/Media creation or update
     * .
     *
     * If process fail at any step, all elements created before are deleted through error handling
     * process.
     */
    async submit() {
      if (this.$refs.form.validate()) {
        // Case of creation of new Point and associated Diagnosis
        if (!this.mortality) {
          await this.createNewPoint()
          // new Point is successfully created
        }
        this.back()
      }
    },

    /**
     * createNewPoint(): Method that create new Point based on forms data (cf. this.pointData)
     *
     * @return {JSON object} as new Point
     *
     * If process fails, error message is displayed in snackBar through error handling process.
     */
    async createNewPoint() {
      try {
        this.pointData.geom.coordinates = [this.lng, this.lat]
        return await this.$axios.$post('mortality/', this.mortalityData)
      } catch (_err) {
        const error = {}
        error.code = errorCodes.create_point.code
        error.msg = $nuxt.$t(`error.${errorCodes.create_point.msg}`)
        // set error message to errorStore and triggers message display through "err" watcher in
        // error-snackbar component
        this.$store.commit('errorStore/setError', error)
        this.back()
      }
    },

    /**
     * createNewDiagnosis(): Method that create new Diagnosis based on forms data(cf.this.mortalityData)
     *
     * @param {BigInt} infrstr_id id of related Insfrastructure (Point)
     *
     * Error handling: A Diagnosis should be created at time of Infrastructure (Point) creation.
     * If Diagnosis creation fails, related Infrastructure (Point) will be deleted.
     * Related Media will also be deleted in this case.
     * Finally, error message is displayed in snackBar through error handling process.
     */

    /**
     * createNewMedia(): Method that create new Media based on component forms data and return the
     * list of Ids of created Media
     *
     * @return {BigInt[]} as new Diagnosis
     *
     * If process fails for at least one Media creation, error message is displayed in snackBar
     * through error handling process. Id of Media for which creation did not fail will be return
     * anyway.
     */
    async createNewMedia() {
      const mediaIdList = []
      // await all Promises be resolved before returning result
      await Promise.all(
        // upc for "util-picture-component": task on each img file of the map
        this.$refs.upc.imgFileObject.map(async (img) => {
          try {
            const formData = new FormData()
            formData.append('storage', img) // fill-in FormData with img file
            // TODO get true date and other form fields below
            formData.append('date', '2022-01-01')
            formData.append('author', 'Bob')
            formData.append('source', 'LPO')
            formData.append('remark', 'Nothing to report')
            // create Media
            const newImg = await this.$axios.$post('media/', formData, {
              headers: {
                accept: 'application/json',
                'Content-Type': 'multipart/form-data',
              },
            })
            mediaIdList.push(newImg.id) // set Media id to mediaIdList
          } catch (_err) {
            const error = {}
            error.code = errorCodes.img_sending.code
            error.msg = $nuxt.$t(`error.${errorCodes.img_sending.msg}`)
            // set error message to errorStore and triggers message display through "err"
            // watcher in error-snackbar component
            this.$store.commit('errorStore/setError', error)
          }
        })
      )
      return mediaIdList
    },
  },
}
</script>