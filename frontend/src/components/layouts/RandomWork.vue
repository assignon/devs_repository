<template>
  <div class="random-core animated fadeIn">
    <div class="work-container animated flipIntX"></div>
    <div class="desc-link">
      <div
        class="desc-container animated fadeInUp"
        style="color: white"
        v-html="desc[0].description.substr(0, 250)"
      ></div>
      <a
        :href="`/work/${$store.state.work.workName}`"
        style="text-decoration: none;color: #00ff8e"
        >read more...</a
      >
    </div>
  </div>
</template>

<script>
import { mapGetters } from "vuex";
export default {
  name: "RandomWork",

  data() {
    return {};
  },

  computed: {
    ...mapGetters({
      works: "work/getWorks",
      desc: "description/getDesc",
    }),
  },

  created() {
    let self = this;
    this.allWorks("default", 0, 0);
    // this.$store.dispatch("work/allWorks", {
    //   url: "works/all_works",
    //   params: { order_by: "default", limit: 0, offset: 0 },
    //   callback: async function(data) {
    //     await self.$store.getters["work/setWorks"](JSON.parse(data));
    //     self.getRandomWork();
    //   },
    // });

     // force getRandomWork() to run only on the home page
      setInterval(() => {
        if(self.$router.history.current.name == 'Home'){
          self.getRandomWork();
        }else{
          clearInterval(self.getRandomWork)
        }
      }, 15000);
  },

  mounted() {
 
  },

  methods: {
    async getRandomWork() {
      // return a random work from works array
      let self = this;
      let workContainer = document.querySelector(".work-container");
      // let descContainer = document.querySelector(".desc-container");
      let randIndex = Math.floor(
        Math.random() * self.$store.getters["work/getWorks"].length
      );
      // get work description
      await self.workDescription(self.works[randIndex].fields.name);

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
        self.$store.state.work.workName = name;
        // check if workContainer already have a child
        if (workContainer.childNodes.length == 0) {
          //add child if there is no child yet
          workContainer.appendChild(workImg);
        } else {
          // remove child
          workContainer.removeChild(workContainer.childNodes[0]);
          //add child
          workContainer.appendChild(workImg);
        }
        // workContainer.appendChild(workName);
        workContainer.addEventListener("click", function() {
          self.$router.push(`/work/${randomWork.fields.name}`);
        });
      }, 10);
    },

    allWorks(orderBy, offset, limit) {
      /*
        get all works from the DB
        params:
          orderBy: [str]: [define the order of the data (ex: default=desc, desc, asc)]
          limit: [int]: [pagination integer]
      */
      let self = this;
      this.$store.dispatch("work/allWorks", {
        url: "works/all_works",
        params: { order_by: orderBy, limit: limit, offset: offset },
        callback: async function(data) {
          console.log(JSON.parse(data));
          await self.$store.getters["work/setWorks"](JSON.parse(data));
          self.getRandomWork();
        },
      });
    },

    workDescription(workName) {
      //work decsription
      let self = this;
      this.$store.dispatch("description/getDescription", {
        url: "description/work_desc",
        params: { work_name: workName },
        callback: function(data) {
          // console.log(data);
          self.$store.getters["description/setDesc"](data);
        },
      });
    },
  },
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
.desc-link {
  display: flex;
  width: 100%;
  height: auto;
  flex-direction: column;
  justify-content: flex-start;
  align-items: flex-start;
  margin-top: 20px;
}
.desc-container {
  width: 100%;
  height: auto;
  display: flex;
  flex-direction: column;
  justify-content: flex-start;
  align-items: flex-start;
}
</style>
