<template>
  <div class="navbar" id="menu" :style="{ height: navHeight }">
    <v-layout row justify-space-around align-center class="nav-layout hidden-sm-and-down">
      <v-flex xs2 sm2 m2 lg2 class="logo-flex">
        <router-link to="/" style="text-decoration: none;">
          <div class="yan-logo">
            <h2>
              Yani
              <span style="font-size: 30px;position: relative;left: 1px;color: white;">c</span>
              <span style="color:white;">:\</span>
              <v-icon style="font-size: 17px;" color="#fff">fas fa-terminal</v-icon>
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
            <span>Aboute</span>
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

        <a href="https://www.github.com/assignon" target="_blank" style="text-decoration: none;">
          <div class="menu-item">
            <!--            <span>Github</span>-->
            <v-icon style="font-size: 25px; color:#fff" class>fab fa-github</v-icon>
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
      <v-flex xs2 sm2 m2 lg2 class="logo-flex" v-if="$router.currentRoute.name != 'Home'">
        <router-link to="/" style="text-decoration: none;">
          <div class="yan-logo">
            <h2>
              Yani
              <span style="font-size: 30px;position: relative;left: 1px;color: #f99138;">c</span>
              <span style="color:#f99138;">:\</span>
              <v-icon style="font-size: 17px;" color="#f99138">fas fa-terminal</v-icon>
            </h2>
          </div>
        </router-link>
      </v-flex>

      <v-flex xs2 sm2 m2 lg2 class="logo-flex" v-if="$router.currentRoute.name == 'Home'">
        <div @click="$vuetify.goTo(0, options)" style="text-decoration: none;cursor: pointer;">
          <div class="yan-logo">
            <h2>
              Yani
              <span style="font-size: 30px;position: relative;left: 1px;color: #f99138;">c</span>
              <span style="color:#f99138;">:\</span>
              <v-icon style="font-size: 17px;" color="#f99138">fas fa-terminal</v-icon>
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
            <span>Aboute</span>
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

        <a href="https://www.github.com/assignon" target="_blank" style="text-decoration: none;">
          <div class="menu-item">
            <!--            <span>Github</span>-->
            <v-icon style="font-size: 25px; color:#fff" class>fab fa-github</v-icon>
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
      <v-flex xs9 md9 class="burgermenu-flex">
        <v-icon
          @click.stop="(drawer = !drawer), animateMeuItems()"
          class
          style="color: #333333;margin-left:20px;"
          medium
        >fas fa-bars</v-icon>
        <h2
          class="ml-3 font-weight-bold"
          style="color:rgb(139,83,255);font-style: italic;"
        >Yanick-Dev</h2>
      </v-flex>
    </v-layout>

    <v-navigation-drawer v-model="drawer" fixed top height="100vh" temporary class="nav-drawer">
      <div class="mobile-menu-flex mt-5" style>
        <router-link to="/" style="text-decoration: none;">
          <div class="mobile-menu-item animated" syle="position: relative; left:-10px;">
            <span class="ml-1 mt-1">Accueille</span>
            <v-icon medium style class>home</v-icon>
          </div>
        </router-link>

        <router-link to="/about" style="text-decoration: none;">
          <div class="mobile-menu-item animated">
            <span>About</span>
            <v-icon style="font-size: 20px;" class>fas fa-address-card</v-icon>
          </div>
        </router-link>

        <router-link to="/contact" style="text-decoration: none;">
          <div class="mobile-menu-item animated">
            <span>Contact</span>
            <v-icon style="font-size: 20px;" class>fas fa-envelope</v-icon>
          </div>
        </router-link>
      </div>
      <v-divider style="width: 200px;" class="mt-3 mb-3"></v-divider>
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
      offset: 0,
      easing: "easeInOutCubic",
      easings: Object.keys(easings),
      // navHeight: this.$router.currentRoute.name == 'Home' ? "100px" : "50px"
      navHeight: "70px"
    };
  },

  created() {
    window.addEventListener("scroll", this.menuScrollAnimation);
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

    // get in the db the count of the products added to the cart
    // productNumber() {
    //   let self = this;
    //   this.$axios
    //     .get(`${this.$store.state.HOST}/api/cart/cart_count/`, {
    //       params: {
    //         shoppingSession: self.$session.get("shoppingSession") //shoppingsession / userId change to real userId when the user is logged
    //       }
    //     })
    //     .then(response => {
    //       this.$store.state.numberOfProduct = response.data;
    //     })
    //     .catch(error => {
    //       console.log(error);
    //     });
    // },
    // async showCart() {
    //   let self = this;
    //   let userId = (this.$session.get('auth')) ? this.$session.get('userId') : this.$session.get("shoppingSession")
    //   await this.$store.commit(
    //     "fetchCartContent",
    //       {userId: userId, arr: self.cartcontent}
    //   );
    //   this.$store.state.cartDrawer = true
    //   // this.$store.commit('showModal', {modalId:'cartModal',top: '100px'})
    // }
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
  border: 1px solid #16032c;
  background-color: #16032c;
  z-index: 5;
}
.nav-layout {
  width: 100%;
  height: 100%;
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
  justify-content: center;
  align-items: center;
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
  height: 60px;
  background-color: #16032c;
  box-shadow: 0 3px 1px -2px rgba(0, 0, 0, 0.2), 0 2px 2px 0 rgba(0, 0, 0, 0.14),
    0 1px 5px 0 rgba(0, 0, 0, 0.12);
  position: fixed;
  top: 0px;
  left: 2px;
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
}

.mobile-menu-flex {
  width: 100%;
  height: auto;
  display: flex;
  flex-direction: column;
  justify-content: flex-start;
  align-items: flex-start;
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

.mobile-menu-item span {
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
}

@media only screen and (max-width: 500px) {
  .navbar {
    margin-bottom: 0px;
  }
}
</style>
