<template>
  <div class="navbar" id="menu" :style="{ height: navHeight }">
    <v-layout
      row
      justify-space-around
      align-center
      class="nav-layout hidden-sm-and-down"
    >
      <v-flex xs2 sm2 m2 lg2 class="logo-flex">
        <router-link to="/" style="text-decoration: none;">
          <div class="yan-logo">
            <h2>
              Yani
              <span
                style="font-size: 30px;position: relative;left: 1px;color: white;"
                >c</span
              >
              <span style="color:white;">:\</span>
              <v-icon style="font-size: 17px;" color="#fff"
                >fas fa-terminal</v-icon
              >
            </h2>
          </div>
        </router-link>
      </v-flex>

      <v-flex xs8 sm8 m8 lg8 class="menu-flex">
        <div
          @click="$vuetify.goTo('#about', options)"
          style="text-decoration: none;cursor: pointer;"
        >
          <div class="menu-item">
            <span>About</span>
            <v-icon style="font-size: 18px;" class>fas fa-address-card</v-icon>
          </div>
        </div>

        <router-link to="/skills" style="text-decoration: none;">
          <div class="menu-item">
            <span>Skills</span>
            <v-icon style="font-size: 18px;" class>fas fa-cogs</v-icon>
          </div>
        </router-link>

        <router-link to="/works" style="text-decoration: none;">
          <div class="menu-item">
            <span>Works</span>
            <v-icon style="font-size: 18px;" class>fas fa-folder</v-icon>
          </div>
        </router-link>

        <div
          @click="$vuetify.goTo('#contact', options)"
          style="text-decoration: none;cursor: pointer;"
        >
          <div class="menu-item">
            <span>Contact</span>
            <v-icon style="font-size: 18px;" class>fas fa-envelope</v-icon>
          </div>
        </div>

        <a
          href="https://www.github.com/assignon"
          target="_blank"
          style="text-decoration: none;"
        >
          <div class="menu-item">
            <!--            <span>Github</span>-->
            <v-icon style="font-size: 25px; color:#fff" class
              >fab fa-github</v-icon
            >
          </div>
        </a>
      </v-flex>
    </v-layout>

    <!--- -- ------------------------------------------ bar menu ------------------------------------------------------------->
    <v-layout
      row
      justify-space-around
      align-center
      style="z-index: 10; display: none"
      class="scroll-nav-layout hidden-sm-and-down animated"
    >
      <v-flex
        xs2
        sm2
        m2
        lg2
        class="logo-flex"
        v-if="$router.currentRoute.name != 'Home'"
      >
        <router-link to="/" style="text-decoration: none;">
          <div class="yan-logo">
            <h2>
              Yani
              <span
                style="font-size: 30px;position: relative;left: 1px;color: #f99138;"
                >c</span
              >
              <span style="color:#f99138;">:\</span>
              <v-icon style="font-size: 17px;" color="#f99138"
                >fas fa-terminal</v-icon
              >
            </h2>
          </div>
        </router-link>
      </v-flex>

      <v-flex
        xs2
        sm2
        m2
        lg2
        class="logo-flex"
        v-if="$router.currentRoute.name == 'Home'"
      >
        <div
          @click="$vuetify.goTo(0, options)"
          style="text-decoration: none;cursor: pointer;"
        >
          <div class="yan-logo">
            <h2>
              Yani
              <span
                style="font-size: 30px;position: relative;left: 1px;color: #f99138;"
                >c</span
              >
              <span style="color:#f99138;">:\</span>
              <v-icon style="font-size: 17px;" color="#f99138"
                >fas fa-terminal</v-icon
              >
            </h2>
          </div>
        </div>
      </v-flex>

      <v-flex xs8 sm8 m8 lg8 class="menu-flex">
        <div
          @click="$vuetify.goTo('#about', options)"
          style="text-decoration: none;cursor: pointer;"
        >
          <div class="menu-item">
            <span>About</span>
            <v-icon style="font-size: 18px;" class>fas fa-address-card</v-icon>
          </div>
        </div>

        <router-link to="/skills" style="text-decoration: none;">
          <div class="menu-item">
            <span>Skills</span>
            <v-icon style="font-size: 18px;" class>fas fa-cogs</v-icon>
          </div>
        </router-link>

        <router-link to="/works" style="text-decoration: none;">
          <div class="menu-item">
            <span>Works</span>
            <v-icon style="font-size: 18px;" class>fas fa-folder</v-icon>
          </div>
        </router-link>

        <div
          @click="$vuetify.goTo('#contact', options)"
          style="text-decoration: none;cursor: pointer;"
        >
          <div class="menu-item">
            <span>Contact</span>
            <v-icon style="font-size: 18px;" class>fas fa-envelope</v-icon>
          </div>
        </div>

        <a
          href="https://www.github.com/assignon"
          target="_blank"
          style="text-decoration: none;"
        >
          <div class="menu-item">
            <v-icon style="font-size: 25px; color:#fff" class
              >fab fa-github</v-icon
            >
          </div>
        </a>
      </v-flex>
    </v-layout>

    <!-- mobile, tablete menu -->
    <v-layout
      row
      justify-space-around
      align-center
      class="mobile-menu-layout hidden-md-and-up animated fadeIn"
    >
      <v-flex xs12 sm12 md12 class="burgermenu-flex">
        <v-icon
          @click.stop="drawer = !drawer"
          class
          style="color: white;margin-left:20px;"
          medium
          >fas fa-bars</v-icon
        >
        <router-link to="/" style="text-decoration: none;">
          <div class="yan-logo">
            <h2>
              Yani
              <span
                style="font-size: 30px;position: relative;left: 1px;color: #f99138;"
                >c</span
              >
              <span style="color:#f99138;">:\</span>
              <v-icon style="font-size: 17px;" color="#f99138"
                >fas fa-terminal</v-icon
              >
            </h2>
          </div>
        </router-link>
        <div class="filters" v-if="$router.currentRoute.name == 'Works'">
          <v-tooltip bottom>
            <template v-slot:activator="{ on, attrs }">
              <v-icon
                medium
                class="asc-icon ml-3 animated bounceIn"
                v-bind="attrs"
                v-on="on"
                @click="orderByAsc()"
                >fas fa-sort-amount-up</v-icon
              >
            </template>
            <span>old to newest</span>
          </v-tooltip>

          <v-tooltip bottom>
            <template v-slot:activator="{ on, attrs }">
              <v-icon
                medium
                class="desc-icon ml-3 animated bounceIn"
                v-bind="attrs"
                v-on="on"
                @click="orderByDesc()"
                >fas fa-sort-amount-down</v-icon
              >
            </template>
            <span>newest to old</span>
          </v-tooltip>

          <v-tooltip bottom>
            <template v-slot:activator="{ on, attrs }">
              <v-icon
                medium
                class="ml-3 animated bounceIn"
                v-bind="attrs"
                v-on="on"
                @click="filtersVisible = !filtersVisible"
                >fas fa-filter</v-icon
              >
            </template>
            <span>filter</span>
          </v-tooltip>
        </div>
      </v-flex>
    </v-layout>

    <v-navigation-drawer
      v-model="drawer"
      fixed
      overlay-color="#54bf8e"
      top
      height="100vh"
      temporary
      class="nav-drawer"
    >
      <router-link to="/" style="text-decoration: none;">
        <div
          class="yan-logo"
          style=" width: auto;height: auto;margin-top: 20px;justify-content: center;align-items: center;"
        >
          <h2 style="color: #36495d;">
            Yani
            <span
              style="font-size: 30px;position: relative;left: 1px;color: #f99138;"
              >c</span
            >
            <span style="color:#f99138;">:\</span>
            <v-icon style="font-size: 17px;" color="#f99138"
              >fas fa-terminal</v-icon
            >
          </h2>
        </div>
      </router-link>

      <v-list rounded class="mt-5">
        <!-- <v-subheader>REPORTS</v-subheader> -->
        <v-list-item-group v-model="mobileMenu" color="#41b883">
          <v-list-item
            class="animated fadeInUp"
            @click="$vuetify.goTo('#about', options), (drawer = false)"
            style="animation-delay: 0.3s;text-decoration: none;cursor: pointer;"
          >
            <v-list-item-icon>
              <v-icon style="" medium class>fas fa-address-card</v-icon>
            </v-list-item-icon>

            <v-list-item-content>
              <v-list-item-title>About</v-list-item-title>
            </v-list-item-content>
          </v-list-item>

          <v-list-item class="animated fadeInUp" style="animation-delay: 0.3s;">
            <v-list-item-icon>
              <v-icon style="" medium class>fas fa-cogs</v-icon>
            </v-list-item-icon>

            <v-list-item-content>
              <router-link
                to="/skills"
                style="text-decoration: none;color: #000"
              >
                <div class="menu-item">
                  <v-list-item-title>Skills</v-list-item-title>
                </div>
              </router-link>
            </v-list-item-content>
          </v-list-item>

          <v-list-item class="animated fadeInUp" style="animation-delay: 0.3s;">
            <v-list-item-icon>
              <v-icon style="" medium class>fas fa-folder</v-icon>
            </v-list-item-icon>

            <v-list-item-content>
              <router-link
                to="/works"
                style="text-decoration: none;color: #000"
              >
                <div class="menu-item">
                  <v-list-item-title>Works</v-list-item-title>
                </div>
              </router-link>
            </v-list-item-content>
          </v-list-item>

          <v-list-item
            class="animated fadeInUp"
            @click="$vuetify.goTo('#contact', options), (drawer = false)"
            style="animation-delay: 0.3s;text-decoration: none;cursor: pointer;"
          >
            <v-list-item-icon>
              <v-icon style="" medium class>fas fa-envelope</v-icon>
            </v-list-item-icon>

            <v-list-item-content>
              <v-list-item-title>Contact</v-list-item-title>
            </v-list-item-content>
          </v-list-item>

          <v-list-item
            class="animated fadeInUp"
            style="animation-delay: 0.3s;text-decoration: none;cursor: pointer;"
          >
            <v-list-item-icon>
              <v-icon style="" medium class>fab fa-github</v-icon>
            </v-list-item-icon>

            <v-list-item-content>
              <a
                href="https://www.github.com/assignon"
                target="_blank"
                style="text-decoration: none;"
              >
                <div class="menu-item">
                  <v-list-item-title>GitHub</v-list-item-title>
                </div>
              </a>
            </v-list-item-content>
          </v-list-item>
        </v-list-item-group>
      </v-list>

      <!-- <v-divider style="width: 200px;" class="mt-3 mb-3"></v-divider> -->
    </v-navigation-drawer>
  </div>
</template>

<script>
import * as easings from "vuetify/es5/services/goto/easing-patterns";
export default {
  name: "navbar",
  components: {},
  data() {
    return {
      activeBtn: 0,
      siteColor: "#8B53FF",
      secondaryNav: false,
      drawer: false,
      duration: 400,
      offset: 25,
      easing: "easeInOutCubic",
      easings: Object.keys(easings),
      // navHeight: this.$router.currentRoute.name == 'Home' ? "100px" : "50px"
      navHeight: "70px",
      mobileMenu: 0 // mobile nav drawer list model
    };
  },

  created() {
    // window.addEventListener("scroll", this.menuScrollAnimation);
    if (window.innerWidth <= 500) {
      // change related works drawer width on mobile
      this.navHeight = "50px";
    }
  },

  computed: {
    target() {
      const value = this[this.type];
      if (!isNaN(value)) return Number(value);
      else return value;
    },

    options() {
      return {
        duration: this.duration,
        offset: this.offset,
        easing: this.easing
      };
    }
  },

  methods: {
    menuScrollAnimation() {
      let scrollValue = document.documentElement.scrollTop;
      let scrollNavLayout = document.querySelector(".scroll-nav-layout");
      if (scrollValue >= 100) {
        scrollNavLayout.style.display = "flex";
        scrollNavLayout.style.transition = "opacity 0.5s linear 0.1s";
        scrollNavLayout.style.opacity = scrollValue / 150;
        scrollNavLayout.classList.add("slideInDown");
      } else if (scrollValue < 100) {
        scrollNavLayout.style.display = "none";
        scrollNavLayout.style.opacity = "0";
      }
    }
  }
};
</script>

<style scoped>
.navbar {
  width: 100%;
  /*height: 100px;*/
  display: flex;
  justify-content: center;
  align-items: center;
  /*margin-bottom: 30px;*/
  z-index: 5;
}
.nav-layout {
  width: 100%;
  height: 100%;
  border: 1px solid #16032c;
  background-color: #16032c;
}

.nav-layout .logo-flex {
  display: flex;
  flex-direction: row;
  justify-content: flex-start;
  align-items: center;
  width: 10%;
  /*position: relative;*/
}

.scroll-nav-layout .logo-flex {
  display: flex;
  justify-content: flex-start;
  align-items: center;
  width: auto;
  height: 100%;
}
.yan-logo {
  display: flex;
  justify-content: flex-start;
  align-items: flex-start;
  width: 100%;
  height: 100%;
  /*position: relative;*/
  /*bottom: 30px;*/
  /*background-image: url("../../../public/img/icons/android-chrome-192x192.png");*/
  /*background-repeat: no-repeat;*/
  /*background-position: center;*/
  /*background-size: contain;*/
}

.yan-logo h2 {
  color: #00ff8e;
}

/*.scroll-yan-logo{*/
/*  background-image: url('../../../public/img/icons/apple-touch-icon-76x76.png');*/
/*  background-size: cover;*/
/*  background-repeat: no-repeat;*/
/*  background-position: center;*/
/*  width: 77px;*/
/*  height: 70px;*/
/*}*/

.nav-layout .menu-flex {
  /*width: 70%;*/
  display: flex;
  flex-direction: row;
  justify-content: flex-end;
  align-items: center;
  /*border: 1px solid blue;*/
}
.scroll-nav-layout .menu-flex {
  display: flex;
  flex-direction: row;
  justify-content: flex-end;
  align-items: center;
}
.menu-item {
  width: 100%;
  height: 100%;
  display: flex;
  flex-direction: row-reverse;
  justify-content: flex-start;
  align-items: flex-start;
  margin-left: 20px;
  margin-right: 20px;
}
.menu-item .v-icon {
  color: #7d7d7d;
}
.menu-flex .menu-item span {
  font-size: 13px;
  color: #fff;
  text-align: center;
  position: relative;
  left: 5px;
  font-weight: bold;
}

.menu-flex .menu-item .v-icon {
  color: white;
}

.menu-flex .menu-item:hover span {
  color: #00ff8e;
}
.menu-flex .menu-item:hover .v-icon {
  color: #00ff8e;
}
.scroll-nav-layout {
  width: 100%;
  height: 50px;
  position: fixed;
  background-color: #16032c;
  top: 0px;
  right: 12px;
  z-index: 3;
  opacity: 0;
  box-shadow: 0 3px 1px -2px rgba(0, 0, 0, 0.2), 0 2px 2px 0 rgba(0, 0, 0, 0.14),
    0 1px 5px 0 rgba(0, 0, 0, 0.12);
}
.mobile-menu-layout {
  width: 100%;
  height: 50px;
  background-color: #16032c;
  box-shadow: 0 3px 1px -2px rgba(0, 0, 0, 0.2), 0 2px 2px 0 rgba(0, 0, 0, 0.14),
    0 1px 5px 0 rgba(0, 0, 0, 0.12);
  position: fixed;
  top: 0px;
  /* left: 2px; */
  z-index: 3;
  overflow-x: hidden;
}
.burgermenu-flex {
  width: 100%;
  height: auto;
  display: flex;
  flex-direction: row;
  justify-content: flex-start;
  align-items: center;
}

.nav-drawer {
  width: 100%;
  /* height: auto; */
  display: flex;
  flex-direction: column;
  justify-content: flex-start;
  align-items: flex-start;
  padding-left: 20px;
  top: 0px;
  z-index: 5;
}

.mobile-menu-flex {
  width: 100%;
  height: auto;
  display: flex;
  flex-direction: column;
  justify-content: flex-start;
  align-items: flex-start;
  border: 1px solid red;
}

.mobile-menu-flex .menu-item span {
  font-size: 16px;
  color: #16032c;
  text-align: center;
  position: relative;
  left: 5px;
  font-weight: bold;
}

.mobile-menu-flex .menu-item .v-icon {
  color: #16032c;
}

.mobile-menu-flex .menu-item:hover span {
  color: #00ff8e;
}
.mobile-menu-flex .menu-item:hover .v-icon {
  color: #00ff8e;
}

.mobile-menu-item {
  width: 100%;
  height: auto;
  display: flex;
  flex-direction: row-reverse;
  justify-content: flex-start;
  align-items: center;
  margin-top: 20px;
}

/* .mobile-menu-item span {
  margin-left: 10px;
  font-size: 16px;
  color: #757575;
  text-align: left;
  font-weight: bold;
}

.mobile-menu-item:hover span {
  color: #8b53ff;
}

.mobile-menu-item:hover .v-icon {
  color: #8b53ff;
} */
.filters {
  width: 50%;
  height: auto;
  display: flex;
  flex-direction: row;
  justify-content: flex-end;
  align-items: flex-end;
}

@media only screen and (max-width: 500px) {
  .navbar {
    margin-bottom: 0px;
  }
  .yan-logo {
    position: relative;
    left: 15px;
    bottom: 5px;
  }

  .yan-logo h2 {
    font-size: 18px;
  }
}
</style>
