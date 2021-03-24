<template>
  <div>

    <b-jumbotron>
      <template #header>Asian Hate Speech Tracker</template>

      <template #lead>

        Percentage of threads on the 4chan board /pol/ which contain <a href="https://hatebase.org/"> asian hate speech </a>

      </template>

      <hr class="my-4">

<!--       <p>
        It uses high level machine learning.
      </p> -->

      <div class="hatecard">

      <b-card
      header="Asian Hate Speech Percentage"
      header-text-variant="white"
      header-tag="header"
      header-bg-variant="dark"
      text-align="center"
      style="max-width: 20rem;"
      >

      <div class="cardpercent" v-if="loadingStatus">
      <h2 class="loadtext" v-if="loadingStatus">Gathering the data, this might take a minute...</h2>
      <b-spinner class="spinner" v-if="loadingStatus" variant="primary" label="Spinning"></b-spinner>
      </div>

      <b-card-text v-else>
        {{ percentage }}
      </b-card-text>
    </b-card>

      </div>
    <div class = "hatecardbutton">
    <b-button variant="primary" @click="getHateSpeechPercentage">Update Data</b-button>
    </div>
<footer class="page-footer font-small mdb-color pt-4">

<h4 class="descrip">This project was created to shine a light on AAPI hate in the aftermath of the tragic shootings in Atlanta, in which six women of Asian descent were shot and killed.</h4>
<h4 class="descrip">/pol/, which stands for 'politically incorrect', is a board on the 4chan website that has become an increasingly popular forum for discussions of extreme political ideologies. It has often been used as a sort of <a href= "https://www.vice.com/en/article/d3nbzy/we-analyzed-more-than-1-million-comments-on-4chan-hate-speech-there-has-spiked-by-40-since-2015"> litmus test </a>to gauge the level of hate certain minority groups are experiencing, though it is in no way a comprehensive measure. We use hatebase.org as our source of <a href="https://hatebase.org/">Asian hate terms</a>. </h4>
<h4 class="descrip">If you have any further questions or would like to contribute to the project, reach out to us at jguo13@gmail.com or leave a comment on the <a href="https://github.com/jguo13/asianhatespeech_project">codebase repository</a></h4>
<p class="createdby">
  Created by Joyce Guo and James Wong
</p>
</footer>
  </b-jumbotron>

</div>
</template>

<script>
  import axios from 'axios';
  export default {
    name: 'HateCard',
    data() {
      return {
        loadingStatus: true,
        percentage: 0.0
      }
    },
    mounted() {
      this.getHateSpeechPercentage();
    },
    methods: {
      getHateSpeechPercentage() {
        this.loadingStatus = true;
        // const path = 'http://0.0.0.0:5000/get_hate/stats'
        const path = 'https://asianhatetrackerproject.com/get_hate/stats';
        axios.get(path)
        .then((res) => {
          this.percentage = res.data.percentage;
          this.loadingStatus = false;
        })
        .catch((error) => {
          console.error(error);
          this.percentage = -1.0;
          this.loadingStatus = false;
        });
      }
    }
  }
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.cardpercent{

  flex-direction: column;
  display: flex;
  align-items: center;
  justify-content: space-around;
  padding-bottom: 40px;
}

.descrip {
  padding-top: 100px;
  padding-right: 300px;
  color: #fff;
}
.card-header {
  background-color: #2ec4b6 !important;
  text-align: center !important;
  font-weight: 400;
  font-size: 3vw;

}
.card-body {
  text-align: center !important;
  font-weight: 400;
  font-size: 15vw;

}
.loadtext{
  color: #0c5cd4 !important;
  padding-bottom: 50px;
}
.b-card{
  border-color: #2ec4b6 !important;
}
.card{
  width: 80%;
  height: 80%;
  max-height: 100% !important;
  max-width: 80% !important;
  border-color: #2ec4b6 !important;
}
.btn-primary {
    color: #fff !important;
    background-color: #ff9f1c !important;
    border-color: #ff9f1c !important; /*set the color you want here*/
}
.createdby{
  padding-top: 100px;
  color:white;
}
.btn-primary:hover, .btn-primary:focus, .btn-primary:active, .btn-primary.active{
    color: #fff !important;
    background-color: #ff7300 !important;
    border-color: #ff7300 !important; /*set the color you want here*/
    box-shadow: 0 0 0 0.2rem rgba(255, 159, 28, 0.5) !important;
}
.data-v-337222ec {
  width: 100vh;
}
.hatecardbutton {
  padding-right: 100px !important;
  margin-top: 10px;
  display: flex;
  align-items: center;
  justify-content: space-around;
}
.hatecard {
  padding-right: 100px !important;
  display: flex;
  align-items: center;
  justify-content: space-around;
  height: 50%;
}
.jumbotron h1{

font-weight: 400;
font-size: 4vw;
color: #fdfffc;
}

.lead {
  color: #fdfffc
}
.jumbotron {


  height: 100%;

  background-color: #011627
}
</style>
