<template>
  <div class="textanimation-core" :style="{ width: w, height: h }"></div>
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
    "display",
  ], //ta=textAlign, fz=fontsize

  data() {
    return {
      totalDelay: 0, // time the text animation take to finish
    };
  },

  created() {},

  mounted() {
    let self = this;
    self.animateBlock();
    // if (self.random) {
    //   // console.log(randomNumber);
    //   let textArrayLen = this.textArray.length;
    //   let randomNumber = Math.floor(Math.random() * textArrayLen);
    //   this.animateText(randomNumber, function(el) {
    //     // el: <p>
    //     console.log(el);
    //     // setTimeout(() => {
    //     //   el.style.display = "none";
    //     // }, self.totalDelay);
    //   });

    //   //   setInterval(() => {
    //   //     let textArrayLen = this.textArray.length;
    //   //     let randomNumber = Math.floor(Math.random() * textArrayLen);
    //   //     this.animateText(randomNumber, function(el) {
    //   //       setTimeout(() => {
    //   //         let childs = el.children;
    //   //         childs.forEach((child) => {
    //   //           child.classList.remove(self.animation);
    //   //           child.classList.add("bounceOut");
    //   //           setTimeout(() => {
    //   //             el.style.display = "none";
    //   //           }, 3000);
    //   //         });
    //   //       }, self.totalDelay);
    //   //     });
    //   //   }, self.totalDelay * 2);
    //   // } else {
    //   //   setInterval(() => {
    //   //     this.animateText();
    //   //   }, 2000);
    // }
  },

  methods: {
    syntaxHighlighting(index, progIndex, keywordsIndex) {
      /*
        change span color to programming language key word color
        params:
          index: [number]: [array index key]
          progIndex: [str]: [array obj base on index]
          keywordsIndex: [str]: [array obj elem]
        doc:
          k: keywords, c: cls, f: fn name, v: variabel, p: fn params, s: string, o: operators
       */

      let colors = [
        {
          P: [ // python
            {
              k: "blue",
              f: "green",
              c: "blue",
              v: "white",
              p: "orange",
              s: "yellow",
              o: "red",
            },
          ],
        },
        {},
      ];

      return colors[index][progIndex][0][keywordsIndex];
    },

    animateBlock(){
      let textContainer = document.querySelector(".textanimation-core");
      let self = this;
      // let indentArr = ['?', '|', '#'];
      let colors = ['#E65100', 'white', 'orange', 'purple', '#009688', '#00BCD4', '#29B6F6', '#00E676']
      // block9divs) width ad margin left
      let blockOpts = [
        // 1 indent = 20px
        {w: '30%', ml: '0px'}, //def
        {w: '55%', ml: '40px'}, //var
        {w: '50%', ml: '40px'}, //if
        {w: '60%', ml: '80px'}, //code
        {w: '55%', ml: '80px'}, //code
        {w: '70%', ml: '80px'}, //code
        {w: '35%', ml: '40px'}, //else
        {w: '65%', ml: '80px'}, //code
        {w: '45%', ml: '80px'}, //code
        {w: '60%', ml: '80px'}, //code
        {w: '50%', ml: '40px'}, // code
        {w: '40%', ml: '40px'}, // return
      ]

      let colorArrayLen = colors.length;

      for (let index = 0; index < 12; index++) {
        const blocks = document.createElement("div");
        let randomNumber = Math.floor(Math.random() * colorArrayLen);

        blocks.style.width = blockOpts[index].w;
        blocks.style.height = "25px";
        blocks.style.marginLeft = blockOpts[index].ml;
        blocks.style.borderRadius = "3px";
        blocks.style.marginBottom = "15px";
        blocks.style.backgroundColor = colors[randomNumber]
        blocks.className = `animated ${self.animation}`;
        // blocks.style.animationDuration = `${index / 10}s`;
        blocks.style.animationDelay = `${index / 3}s`;
        textContainer.appendChild(blocks);
      }
    },

    animateText(randomIndex = 0, callback) {
      /*
            text typing animation
            params:
                randomIndex: [int]: [generate random int for the text array index, default: 0]
            doc: indentation signs
                ?: 1 tabulation
                |: 1 break
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
          spans.style.animationDelay = `${i / 30}s`;
          spanArray.push(spans);
          p.appendChild(spans);

          this.totalDelay += i / 10;

          if (t[i] == "?") {
            spans.innerHTML = " "; // remove ?
            // p.innerHTML += "<br/>";
            p.innerHTML += "&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;";
          } else if (t[i] == "|") {
            spans.innerHTML = " "; // remove |
            // p.innerHTML += "<br/>";
            p.innerHTML += "<br/>";
          }
          // else if (t[i] == "#") {
          //   spans.innerHTML = " "; // remove #
          //   p.innerHTML += "<br/>";
          // }
          else if (t[i] == "%") {
            let index = t[i + 1]; // array index
            let progIndex = t[i + 2]; // prog lang name
            let kwIndex = t[i + 3]; // prog lang keyword type

            // spans.innerHTML = " "; // remove %
            // spans.nextSibling.nextSibling.innerHTML = " ";
            // spans.nextSibling.nextSibling.nextSibling.innerHTML = " ";
            // spans.nextSibling.nextSibling.nextSibling.nextSibling.innerHTML =
            //   " ";
            // if (t[i + 1] == index) {
            //   console.log(spans);
            // } else if (t[i + 2] == progIndex) {
            //   spans.innerHTML = " "; // remove prog index
            // } else if (t[i + 3] == kwIndex) {
            //   spans.innerHTML = " "; // remove keyword index
            // }

            console.log(self.syntaxHighlighting(index, progIndex, kwIndex));
            spanArray.forEach((s) => {
              // s.style.color = "green";
              s.style.color = self.syntaxHighlighting(
                index,
                progIndex,
                kwIndex
              );
            });
            //empty array
            spanArray = [];
          }

          // console.log(this.totalDelay);
        }

        try {
          textContainer.appendChild(p);
          // console.log(p.textContent);
        } catch (TypeError) {
          return false;
        }
        callback(p);
        // console.log(p);
      });
    },
  },
};
</script>

<style scoped>
.cover {
  width: 100%;
  height: 100%;
  display: flex;
  display: flex;
  justify-content: center;
  align-items: center;
}
.textanimation-core {
  /* width: 50%;
  height: 100%; */
  display: flex;
  /* color: white; */
  /* border: 1px solid whitesmoke; */
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: flex-start;
  overflow: hidden;
}
@media only screen and (max-width: 500px) {
  .textanimation-core {
    width: 100%;
    /* overflow: hidden; */
  }
}
</style>
