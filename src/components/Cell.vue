<template>
  <div class="cell">
    <a :href="item.url" target="_blank">
      <div class="left">
        <img :src="item.img" alt="">
      </div>
      <div class="right">
        <div class="title">{{ item.title }}</div>
        <div class="platform">
          <!-- <img class="icon" src="../assets/Amazon.png" /> -->
          <img class="icon" :src="img_url(item.platform)" />
          <!-- <img :src="'../assets/' + item.platform + '.png'" /> -->
        </div>
        <div class="price">
          <div class="jp">{{ price.jp }}</div>
          <div class="tw">{{ price.tw }}</div>
        </div>
      </div>
    </a>
  </div>
</template>

<script>
export default {
  name: 'Cell',
  props: {
    rate: Number,
    item: Object,
    country: String
  },
  computed: {
    price () {
      const res = {}
      if(this.country === "jp") {
        res.jp = this.item.price
        res.tw = this.rate ? parseInt(this.item.price / this.rate) : 'N/A'
      }
      else {
        res.tw = this.item.price
        res.jp = this.rate ? parseInt(this.item.price * this.rate) : 'N/A'
      }
      res.jp = res.jp.toLocaleString()
      res.tw = res.tw.toLocaleString()
      return res
    }
  },
  methods: {
    img_url (platform) {
      return require('../assets/' + platform + '.png')
    }

  }
}
</script>

<style lang="scss">
.cell {
  /* width: 400px; */
  width: calc(100% - 20px);
  padding: 8px;
  border: solid 1px transparent;
    &:hover {
      border-color: red;
    }
  a {
    text-decoration: none;
    color: black;
    &:visited {
      color: #2355a5;
    }
    .left {
      display: inline-block;
      max-width: 120px;
      width: 100%;
      text-align: center;
      vertical-align: middle;
      img {
        /* max-width: 100%; */
        width: 100%;
        max-height: 200px;
      }
    }
    .right {
      display: inline-block;
      width: calc(100% - 128px);
      vertical-align: top;
      padding: 4px;
      @include sp {
        display: block;
        width: 100%;
      }
      .title {
        font-size: 12px;
      }
      .platform {
        display: inline-block;
        margin-right: 6px;
        img {
          max-width: 30px;
        }
      }
      .price {
        display: inline-block;
        font-weight: bold;
        .jp {
          color: #F06060;
          &:before {
            content: "¥ "
          }
        }
        .tw {
          color: #0077AA;
          &:before {
            content: "$ "
          }
        }
      }
    }
  }
}
</style>
