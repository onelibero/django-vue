<template>
  <div>
  <p @click="prev()" class="ssss">>>></p>
  <!-- 动漫展示 -->
  <div class="zong">
    <div class="zuo">
      <img :src="comic.cover" class="img">
      <div class="you">
         <p>昵称:{{comic.comicName}}</p>
         <p>地区:{{ comic.region }}</p>
         <p>标签:{{ comic.label }}</p>
         <p>年份:{{ comic.year }}</p>
         <p>热度:{{ comic.popularity }}</p>
         <p>最近更新:{{ comic.updateTime }}</p>
         <p>总集数:{{ comic.number }}</p>
         <p>更新到多少集:{{ comic.remark }}</p>
         <p @click="like()" class="xuan">☆</p>
       </div>			
      </div>
    <div class="bianjie"></div>
    
<!-- 输入评论 -->


  </div>
</div>
</template>

<script>
export default {
  name: 'HelloWorld',
  props: {
    msg: String
  },
data(){
    return {
      comic:this.$TestData.comic,
    }
  },
  created(){
    this.comic=this.$route.query.item
  },
  methods:{
    prev(){
      this.$router.go(-1)
    }
  }
    
   
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.ssss{
cursor: pointer;
  background-color: unset;
}
.xuan{
cursor: pointer;
  background-color: unset;
}
.kreply{
cursor: pointer;
  background-color: unset;
color: #0cbcf2;
margin-left: 10px;
font-size: 12px;
font-weight: 1000;
}

.shanchu{
margin-left: 10px;
}
.kmiaoshu{
font-size: 12px;
}
.kname{
color: red;
margin-top: 10px;
font-size: 15px;
font-weight: 1000;
}
.kimg{
margin-top: 20px;
height: 60px;
width: 60px;
border-radius: 50%;
}

.sss{

width: 100px;
height: 100px;
display: flex;
flex-direction: column;
}
.fu{
display: flex;
flex-direction:row ;
}
.shuru01{
margin-left: 150px;
height: 100px;
width: 300px;
}
.shuru{
width: 100%;
display: flex;
flex-direction: column;
margin-bottom: 200px;
}
input{
width: 400px;
height: 100px;

}
button{
margin-top: 10px;
margin-left: 250px;
width: 100px;
}
.hhe{
display: flex;
flex-direction: row;
}
.reply01{
cursor: pointer;
  background-color: unset;
font-size: 10px;
width: 20px;
height: 5px;
margin-left: 10px;
margin-top: 25px;
border: 0px;
}
.reply{
cursor: pointer;
  background-color: unset;
color: #0cbcf2;
margin-top: 28px;
margin-left: 10px;
}
.bianjie01{
height: 0px;
background-color: #000;
width: 1000px;
border:1px solid #000;
}
.comicimg{
margin-top: 15px;
margin-left: 5px;
width: 90px;
height: 90px;
border-radius: 50%;
}
.one{
width: 1200px;
height: 120px;
margin-top: 10px;
display: flex;
flex-direction: row;
}
.youu{
margin-left: 20px;
}
.label{
font-weight: 1000;
margin-top: 10px;
color: #3c3a3a;
background-image: linear-gradient(to top, #fbc2eb 0%, #a6c1ee 100%);
}
.time{
width: 100px;
margin-top: 30px;
font-size: 10px;
color: #1d8ccc;
}
.kfudong{
width: 700px;
text-align: left;
margin-left: 10px;
display: flex;
flex-direction: row;
}
.fudong{
width: 700px;
text-align: left;
margin-left: 10px;
}
.name{
color: red;
margin-top: 30px;
font-weight: 1000;
}
.miaoshu{
font-size: 15px;
}
.pagelist{
height: 300px;
overflow-y: auto;
}
.you{
border:1px solid #e7edec;
margin-left: 10px;
width: 300px;
height: 400px;
background-color: #ffffff;
}
.bianjie{
width: 1400px;
border:1px solid #000;
}
.zong{
display: flex;
flex-direction: column;
width: 100%;
height: 100%;
justify-content: center; /*水平居中*/
  align-items: Center; /*垂直居中*/
}
.zuo{
margin-top: 30px;
width: 500px;
height: 500px;
display: flex;
flex-direction: row;
}
.img{
margin-top: 30px;
width: 250px;
height: 350px;
border-radius: 2%;
}
</style>
