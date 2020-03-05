<template>
  <div id="search">
    <div id="inputs">
      <input id="jp" type="text" v-model="jp_word" :class="{ error: jp_empty }"
             @keydown.enter="do_search"
             placeholder="Japanese or model number">
      <input id="tw" type="text" v-model="tw_word" :class="{ error: tw_empty }"
             @keydown.enter="do_search"
             placeholder="Chinese or model number">
    </div>
    <div id="btn_container">
      <div id="btn" @click="do_search">
        Search
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Search',
  props: {
    func: Function
  },
  data() {
    return {
      jp_word: '',
      tw_word: '',
      jp_empty: false,
      tw_empty: false
    }
  },
  methods: {
    do_search(event) {
      if (event.keyCode !== 13) return
      this.jp_empty = this.jp_word === ''
      this.tw_empty = this.tw_word === ''
      if(this.jp_empty || this.tw_empty) return
      this.func(this.jp_word, this.tw_word)
    }
  }
}
</script>

<style lang="scss">
$main_color: #293b6a;
#search {
  margin: 4px 0;
  #inputs {
    display: inline-block;
    width: calc(100% - 78px);
    input[type="text"] {
      width: calc(50% - 8px);
      border: 2px solid #aaa;
      border-radius: 4px;
      margin-right: 6px;
      outline: none;
      padding: 5px;
      font-size: 16px;
      box-sizing: border-box;
      &.error {
        border-color: red;
      }
      @include sp {
        display: block;
        width: calc(100% - 8px);
        margin-bottom: 4px;
      }
    }
  }
  #btn_container {
    display: inline-block;
    vertical-align: top;
    #btn {
      width: 48px;
      text-align: center;
      vertical-align: middle;
      border: 2px solid $main_color;
      font-size: 12px;
      background-color: $main_color;
      color: white;
      text-decoration: none;
      font-weight: bold;
      padding: 5px 10px;
      border-radius: 4px;
      transition: .4s;
      &:hover {
        cursor: pointer;
      }
      @include sp {
        height: 38px;
        padding-top: 20px;
      }
    }
  }
}
</style>
