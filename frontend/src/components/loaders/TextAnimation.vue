<template>
  <div class="textanimation-core" :style="{width: w, height: h}"></div>
</template>

<script>
export default {
  name: "TextAnimation",

  props: [
    "textArray",
    "w",
    "h",
    "animation",
    "color",
    "fs",
    "ta",
    "random",
    "interval",
    "timeout",
    "display"
  ], //ta=textAlign, fz=fontsize

  data() {
    return {};
  },

  created() {},

  mounted() {
    let self = this;
    if (this.random) {
      // console.log(randomNumber);
      let textArrayLen = this.textArray.length;
      let randomNumber = Math.floor(Math.random() * textArrayLen);
      this.animateText(randomNumber, function(el) {
        setTimeout(() => {
          el.style.display = "none";
        }, self.interval);
      });
      setInterval(() => {
        let textArrayLen = this.textArray.length;
        let randomNumber = Math.floor(Math.random() * textArrayLen);
        this.animateText(randomNumber, function(el) {
          setTimeout(() => {
            let childs = el.children;
            childs.forEach(child => {
              child.classList.remove(self.animation);
              child.classList.add("bounceOut");
              setTimeout(() => {
                el.style.display = "none";
              }, 3000);
            });
          }, self.timeout);
        });
      }, self.interval);
    } else {
      setInterval(() => {
        this.animateText();
      }, 2000);
    }
  },

  methods: {
    animateText(randomIndex = 0, callback) {
      /*
            text typing animation
            params:
                randomIndex: [int]: [generate random int for the text array index, default: 0]
            doc: indentation signs
                ?: 1 break and 1 tabulation
                |: 1 break and 2 tabulations
                #: 1 break
        */
      let textContainer = document.querySelector(".textanimation-core");
      let self = this;
      let spanArray = [];

      this.textArray[randomIndex].forEach((t, index) => {
        let p = document.createElement("p");
        p.className = "code-line animated fadeInUp";
        p.style.display = self.display;
        // p.style.flexDirection = "column";
        p.style.animationDelay = `${index}s`;
        p.style.fontSize = this.fs;
        p.style.textAlign = this.ta;
        p.style.fontWeight = "bold";
        p.style.color = this.color;
        p.style.with = "100%";
        p.style.margin = "auto";

        for (let i = 0; i < t.length; i++) {
          let spans = document.createElement("span");
          spans.textContent = t[i];
          spans.classList.remove("bounceOut");
          spans.className = `animated ${self.animation}`;
          spans.style.animationDelay = `${i / 7}s`;
          spanArray.push(spans)
          p.appendChild(spans);

          if (t[i] == "?") {
            p.innerHTML += "<br/>";
            p.innerHTML += "&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;";
          } else if (t[i] == "|") {
            p.innerHTML += "<br/>";
            p.innerHTML +=
              "&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;";
          } else if (t[i] == "#") {
            p.innerHTML += "<br/>";
          }else if(t[i] == '%'){
            spanArray.forEach(s => {
              s.style.color = 'blue';
            })
            spanArray = [];
          }
        }
        try {
          textContainer.appendChild(p);
          console.log(p.textContent)
        } catch (TypeError) {
          return false;
        }
        callback(p);
        // console.log(p);
      });
    }
  }
};
</script>

<style scoped>
.textanimation-core {
  /* width: 50%;
  height: 100%; */
  display: flex;
  /* color: white; */
  /* border: 1px solid whitesmoke; */
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}
</style>