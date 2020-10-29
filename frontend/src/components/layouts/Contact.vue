<template>
  <v-layout class="contact-layout">
    <v-flex xs12 sm12 md6 lg6 xl6 class="map-flex hidden-sm-and-down">
      <div class="map-container">
        <!--        <iframe-->
        <!--          src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d39032.8801596525!2d4.648319085932059!3d52.30593070344154!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x47c5e7afa59ae60d%3A0x3f11830627093e83!2sHoofddorp!5e0!3m2!1sfr!2snl!4v1587240275749!5m2!1sfr!2snl"-->
        <!--          width="100%"-->
        <!--          height="100%"-->
        <!--          frameborder="0"-->
        <!--          style="border:0;"-->
        <!--          allowfullscreen-->
        <!--          aria-hidden="false"-->
        <!--          tabindex="0"-->
        <!--        ></iframe>-->
        <div class="map-overlay">
          <div>
            <h1 class="mb-5" style="color: white;">Contact Me</h1>
            <v-icon medium class="mt-5 mb-1" color="white">fas fa-at</v-icon>
            <p class="mb-5">yanick007assignon@gmail.com</p>
            <v-icon medium class="mb-1 mt-2" color="white"
              >fas fa-phone-alt</v-icon
            >
            <p>0618874429</p>
          </div>
        </div>
      </div>
    </v-flex>

    <v-flex xs12 sm12 md6 lg6 xl6 class="form-flex animated fadeIn">
      <h1
        class="mb-5 font-weight-bold"
        data-aos="fade-up"
        data-aos-duration="500"
      >
        Get in touch
      </h1>
      <v-divider
        width="20%"
        color="#16032c"
        style="margin-top:-15px;margin-bottom:20px;"
      ></v-divider>
      <p class="form-err-msg animated fadeInUp" v-show="contactFormErr"></p>
      <v-form class="mt-5 contact-form animated" ref="form" v-if="!emailSended">
        <v-text-field
          v-model="name"
          :rules="[rules.required]"
          label="Name*"
          required
          outlined
          data-aos="fade-up"
          data-aos-delay="150"
          data-aos-duration="500"
        ></v-text-field>
        <v-text-field
          v-model="email"
          type='email'
          :rules="emailRules"
          label="Email*"
          required
          outlined
          data-aos="fade-up"
          data-aos-delay="300"
          data-aos-duration="500"
        ></v-text-field>
        <v-textarea
          class="mx-2"
          label="Message me*"
          rows="5"
          color="#8B53FF"
          flat
          v-model="messageValue"
          :rules="[rules.required]"
          style="line-height: 22px;"
          outlined
          data-aos="fade-up"
          data-aos-delay="450"
          data-aos-duration="500"
        />
        <div class="btn-container">
          <v-btn
            depressed
            height="40"
            width="30%"
            class="fot-weight-bold white--text"
            color="#16032c"
            @click="sendMail()"
          >
            <v-icon medium left class="ml-1">fas fa-paper-plane</v-icon>SEND
          </v-btn>
        </div>
      </v-form>
      <div class="email-sended animated fadeIn" v-if="emailSended">
        <v-icon style='font-size:50px;' color='#54bf8e' class='mb-3'>fas fa-check-circle</v-icon>
        <p class="animated fadeInUp">
          <strong>Thanks {{ name }},</strong> I receive your email and i will response shortly...
        </p>
      </div>
    </v-flex>
  </v-layout>
</template>

<script>
export default {
  name: "Contact",

  data() {
    return {
      messageValue: "", // contact meg field model
      email: "", // contact email field model
      name: "", // contact name field model
      rules: {
        required: value => !!value || "This field is required",
        min: v => v.length >= 8 || "8 characters minimal",
        emailMatch: () => "Email and password don't match"
      },
      emailRules: [
        v => !!v || "Email is required",
        v => /.+@.+/.test(v) || "Email is not valid"
      ],
      emailSended: false,
      contactFormErr: false
    };
  },

  created() {},

  methods: {
    sendMail() {
      let self = this;
      let formErrMsg = document.querySelector(".form-err-msg");
      let validationErrMsg = document.querySelector('.v-messages__message');

      if (self.name != "" && self.email != "" && self.messageValue != "") {
        if(!document.body.contains(validationErrMsg)){
          self.contactFormErr = false;
          this.$store.dispatch("sendmail", {
            url: "works/sendmail",
            params: {
              name: self.name,
              email: self.email,
              message: self.messageValue
            },
            callback: function(data) {
              console.log(data);
              // if(data.sended){
                self.msgReceive();
              // }
            }
          });
          self.msgReceive();
        }else{
          this.contactFormErr = true;
          formErrMsg.innerHTML = validationErrMsg.textContent;
        }
      } else {
        this.contactFormErr = true;
        formErrMsg.innerHTML = "Fields are empty";
      }
    },

    msgReceive() {
      let self = this;
      this.emailSended = true;
      setTimeout(function() {
        self.emailSended = false;
      }, 7000);
      self.$refs.form.reset();
    }
  }
};
</script>

<style scoped>
.contact-layout {
  width: 100%;
  height: 100%;
  display: flex;
  flex-direction: row;
  justify-content: center;
  align-content: center;
}

.map-flex {
  height: 100%;
  display: flex;
  justify-content: center;
  align-items: center;
  overflow: hidden;
}

.map-container {
  width: 51%;
  height: 100vh;
  display: flex;
  justify-content: center;
  align-items: center;
  position: absolute;
  bottom: 0px;
}

.map-overlay {
  width: 90%;
  height: 90%;
  border-radius: 5px;
  background-color: #16032c;
  /*opacity: 0.6;*/
  position: absolute;
  display: flex;
  justify-content: center;
  align-items: center;
}

.map-overlay div {
  width: 50%;
  height: 90%;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: flex-start;
}

.map-overlay p {
  color: white;
  font-size: 17px;
  font-weight: bold;
}

.form-flex {
  height: 100%;
}

.form-flex {
  width: 100%;
  height: 100%;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}

.form-flex .v-form {
  width: 100%;
  height: auto;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}

.form-flex .v-form .v-text-field {
  width: 80%;
  height: auto;
}

.btn-container {
  width: 80%;
  height: auto;
  display: flex;
  justify-content: flex-end;
  align-items: center;
  margin-top: -15px;
}
.email-sended {
  width: 100%;
  height: auto;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}
.email-sended p {
  text-align: center;
  font-size: 17px;
  width: 100%;
  height: auto;
}
.form-err-msg {
  text-align: center;
  font-size: 17px;
  width: 100%;
  height: auto;
  color: red;
}

@media only screen and (max-width: 500px) {
  .contact-layout {
    flex-direction: column;
  }
}
</style>