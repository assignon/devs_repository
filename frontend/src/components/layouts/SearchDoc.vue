<template>
  <v-dialog v-model="$store.state.searchDialog" max-width="700px">
    <div class="search-dialog-container" style="background-color: white;">
      <h4 class="mb-3">
        The search engine offers different ways and combinations to make more
        efficient searching and finding projects.
      </h4>
      <v-list>
        <v-list-item-group v-model="$store.state.searchDocList" color="#41b883">
          <v-list-item>
            <v-list-item-content>
              <p>
                project
                <strong>type(s)</strong>,
                <strong>programming language(s)</strong>,
                <strong>tags</strong>
                <br />e.g.
                <br />
                <kbd>website</kbd>
              </p>
            </v-list-item-content>
          </v-list-item>
          <v-list-item>
            <v-list-item-content>
              <p>
                <strong>Combining</strong> queries <br />e.g.
                <br />
                <kbd>website+app+...</kbd> or
                <kbd>website,app,pwa,...</kbd>
              </p>
            </v-list-item-content>
          </v-list-item>
          <v-list-item>
            <v-list-item-content>
              <p>
                Search projects
                <strong>before (&lt;)</strong>, <strong>after (>)</strong> or on
                a <strong>specific (=)</strong> date <br />e.g.
                <br />
                <kbd>>2020,09,13</kbd> or <kbd>&lt;2020</kbd> or
                <kbd>=2020,09</kbd>
              </p>
            </v-list-item-content>
          </v-list-item>
          <v-list-item>
            <v-list-item-content>
              <p>
                <strong>Combining</strong> queries and dates <br />e.g.
                <br />
                <kbd>website,pwa> 2020,09,13</kbd> or
                <kbd>website&lt;2020</kbd> or
                <kbd>website+pwa=2020,09</kbd>
              </p>
            </v-list-item-content>
          </v-list-item>
          <v-list-item>
            <v-list-item-content>
              <p>
                Search by<strong> programming languages</strong> <br />e.g.
                <br />
                <kbd>python</kbd> or <kbd>python,vue,...</kbd> or
                <kbd>php+javascript+...</kbd>
              </p>
            </v-list-item-content>
          </v-list-item>
          <v-list-item>
            <v-list-item-content>
              <p>
                <strong>built-in</strong> key words <br />e.g.
                <br />
                <kbd>newest</kbd> and
                <kbd>oldest</kbd>
              </p>
            </v-list-item-content>
          </v-list-item>
        </v-list-item-group>
      </v-list>
      <p>
        <span style="color: magenta,font-weight:bold">i:</span> avoid putting
        spaces between words during combined searches. <br />Do:
        <span style>website,app,cli,...</span>
        <br />Not:
        <span style="text-decoration: line-through"
          >website, app, api, ...</span
        >
        <br />
      </p>
      <p>
        projects
        <strong>types</strong> values: website, mobile, app, cli, desktop app,
        ...
      </p>
      <p>
        projects
        <strong>tags</strong> values: cli, command line, cmd, terminal, site,
        pwa, responsive, programming language packages(e.g. colorama, pillow,
        vuetify, ...)
      </p>
    </div>
  </v-dialog>
</template>

<script>
export default {
  name: "SearchDocumentation",
  //   props: ["dialogStatus", "descMenuModel"],

  computed: {},

  data() {
    return {};
  },

  created() {},

  methods: {},
};
</script>

<style scoped>
.search-dialog-container {
  width: 100%;
  height: auto;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-content: center;
  padding: 20px;
}
.search-dialog-container p {
  color: #1b1127;
}
.v-list-item__content {
  width: 100%;
  height: auto;
  display: flex;
  flex-direction: row;
  justify-content: center;
  align-content: center;
  padding: 0px;
}
.v-list-item__content p {
  width: 90%;
  text-align: left;
  font-size: 16px;
  color: #1b1127;
}
.v-application kbd {
  background-color: #54bf8e;
  padding: 2px;
  margin: 2px 0px 2px 0px;
}
</style>
