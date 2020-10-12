<template>
  <div class="random-core animated fadeIn">
    <div class="work-container animated flipInX"></div>
    <div class="desc-container animated fadeInUp"></div>
  </div>
</template>

<script>
import { mapGetters } from "vuex";
export default {
  name: "RAndomWork",

  data() {
    return {};
  },

  computed: {
    ...mapGetters({
      works: "work/getWorks",
      desc: "description/getDesc"
    })
  },

  created() {
    let self = this;
    this.$store.dispatch("work/allWorks", {
      url: "works/all_works",
      params: { order_by: "default", limit: 0, offset: 0 },
      callback: function(data) {
        self.$store.getters["work/setWorks"](JSON.parse(data));
      }
    });

    // console.log(this.desc);

    // this.getRandomWork();
  },

  mounted() {
    let self = this;
    // setInterval(() => {
    //   //   document.querySelector(".work-container").innerHTML = "";
    //   //   document.querySelector(".desc-container").innerHTML = "";
    //   self.getRandomWork();
    // }, 10000);
    self.getRandomWork();
  },

  methods: {
    getRandomWork() {
      // return a random work from works array
      let self = this;
      let randomCore = document.querySelector(".random-core");
      let workContainer = document.querySelector(".work-container");
      let descContainer = document.querySelector(".desc-container");
      let randIndex = Math.floor(
        Math.random() * self.$store.getters["work/getWorks"].length
      );

      // create html element
      setTimeout(() => {
        let randomWork = self.works[randIndex];
        let name = randomWork.fields.name;
        let workImg = document.createElement("div");
        workImg.className = "work-img";
        workImg.style.backgroundImage = `url(${require(`../../../../media/${randomWork.fields.image}`)})`;
        workImg.style.width = "100%";
        workImg.style.height = "85%";
        workImg.style.backgroundRepeat = "no-repeat";
        workImg.style.backgroundPosition = "center";
        workImg.style.backgroundSize = "cover";
        workImg.style.borderRadius = "3px";

        let workName = document.createElement("h4");
        workName.className = "work-name";
        workName.textContent = name;
        workName.style.textAlign = "center";
        workName.style.color = "white";
        workName.style.position = "relative";
        workName.style.top = "10px";
        // work decsription
        let descriptionContainer = document.createElement("p");
        descriptionContainer.style.width = "90%";
        descriptionContainer.style.height = "auto";
        descriptionContainer.style.fontSize = "15px";
        descriptionContainer.style.color = "white";

        self.workDescription(name);
        let descriptionObj = self.desc;

        descriptionObj.forEach(data => {
          let descPart = data.description.substr(0, 250);
          console.log(descPart);
          descriptionContainer.innerHTML += descPart + "...";
        });
        // add animation
        // randomCore.classList.add("fadeIn");
        // workContainer.classList.add("zoomIn");
        // descContainer.classList.add("fadeInUp");
        // append work html element
        workContainer.appendChild(workImg);
        workContainer.appendChild(workName);
        workContainer.addEventListener("click", function() {
          self.$router.push(`/work/${randomWork.fields.name}`);
        });
        // append work description
        descContainer.appendChild(descriptionContainer);
        // append html elements to the dom
        randomCore.appendChild(workContainer);
        randomCore.appendChild(descContainer);
      }, 1000);
      //
      //   setTimeout(() => {
      //     // randomCore.classList.remove("fadeIn");
      //     // workContainer.classList.remove("zoomIn");
      //     // descContainer.classList.remove("fadeInUp");
      //   }, 8000);
    },

    workDescription(workName) {
      //work decsription
      let self = this;
      this.$store.dispatch("description/getDescription", {
        url: "description/work_desc",
        params: { work_name: workName },
        callback: function(data) {
          console.log(data);
          self.$store.getters["description/setDesc"](data);
        }
      });
    }
  }
};
</script>
<style scoped>
.random-core {
  width: 100%;
  height: auto;
  display: flex;
  flex-direction: column;
  justify-content: flex-start;
  align-items: flex-start;
  margin-bottom: 45px;
}
.work-container {
  width: 250px;
  height: 250px;
  display: flex;
  flex-direction: column;
  justify-content: flex-start;
  align-items: center;
  border: 2px solid #16032c;
  background-color: #16032c;
  border-radius: 5px;
  cursor: pointer;
}
.work-container:hover {
  transition: transform 0.2s linear 0s;
  transform: scale(0.9, 0.9);
}
.works-img {
  width: 100%;
  height: 80%;
  background-repeat: no-repeat;
  background-position: center;
  background-size: cover;
  border-radius: 3px;
}
.works-name {
  text-align: center;
  color: white;
}
.desc-container {
  width: 100%;
  height: auto;
  display: flex;
  justify-content: flex-start;
  align-items: flex-start;
  margin-top: 20px;
}
</style>