<template>
  <div id="main">
    <div id="container">
      <Search :func="search" />
      <div id="rate">
        <div id="title">Rate(TWD/JPY):</div>
        <div id="value">{{ rate }}</div>
      </div>
      <List :items="jp_items" country="jp" :rate="rate" />
      <List :items="tw_items" country="tw" :rate="rate" />
    </div>
  </div>
</template>

<script>
import List from './List.vue'
import Search from './Search.vue'
export default {
  name: 'Main',
  components: {
    List,
    Search
  },
  data() {
    return {
      jp: [],
      tw: [],
      rate: 3.5,
      items: {
        jp: {
          Amazon: [],
          Mercari: [],
          Rakuma: []
        },
        tw: {
          Shopee: [],
          Ruten: []
        }
      },
      res_items: []
    }
  },
  computed: {
    jp_items() {
      return this.get_items('jp')
    },
    tw_items() {
      return this.get_items('tw')
    }
  },
  methods: {
    search(jp_word, tw_word) {
      Object.keys(this.items.jp).forEach(key => {
        this.items.jp[key] = []
        this.$axios.get('/api/search/' + key + '?word=' + jp_word)
          .then(res => {
            this.items.jp[key] = res.data.results
          })

      })
      Object.keys(this.items.tw).forEach(key => {
        this.items.tw[key] = []
        this.$axios.get('/api/search/' + key + '?word=' + tw_word)
          .then(res => {
            this.items.tw[key] = res.data.results
          })

      })
    },
    get_items(country) {
      const res = []
      const keys = Object.keys(this.items[country])
      const max = Math.max.apply(Math, keys.map(key => {
        return this.items[country][key].length
      }))
      for(let i = 0; i < max; i++) {
        keys.forEach(key => {
          const list = this.items[country][key]
          if(i < list.length) {
            const item = list[i]
            item.platform = key
            res.push(item)
          }
        })
      }
      return res
    }
  },
  mounted() {
    this.$axios.get('/api/rate')
      .then(res => {
        this.rate = res.data.results
      })
  }
}
</script>

<style lang="scss">
#main {
  text-align: center;
  #container {
    text-align: left;
    display: inline-block;
    max-width: 1000px;
    width: 100%;
    #rate {
      font-size: 13px;
      letter-spacing: 2.4px;
      margin: 8px 0;
      #title {
        width: 160px;
        display: inline-block;
        background: #5c9ee7;
        color: white;
        text-align: center;
        padding: 5px 0;
      }
      #value {
        display: inline-block;
        width: auto;
        width: calc(100% - 178px);
        background: #f1f8ff;
        font-weight: bold;
        padding: 5px 0 5px 12px;
      }
    }
  }
  .list {
    display: inline-block;
    width: calc(50%);
  }
}
</style>
