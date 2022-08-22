<template>
  <div>
    <div>
      <button @click="printEditorHtml">print html</button>
      <button @click="insertTextHandler">insert text</button>
      <button @click="disableHandler">disable</button>
    </div>
    <div style="border: 1px solid #ccc; margin-top: 10px;">
      <!-- 工具栏 -->
      <Toolbar
        style="border-bottom: 1px solid #ccc"
        :editor="editor"
        :defaultConfig="toolbarConfig"
      />
      <!-- 编辑器 -->
      <Editor
        style="height: 400px; overflow-y: hidden;"
        :defaultConfig="editorConfig"
        v-model="html"
        @onChange="onChange"
        @onCreated="onCreated"
        @customPaste="customPaste"
      />
    </div>
    <div style="margin-top: 10px;">
      <textarea
        v-model="html"
        readonly
        style="width: 100%; height: 200px; outline: none;"
      ></textarea>
    </div>
  </div>
</template>

<script>
import { Editor, Toolbar } from '@wangeditor/editor-for-vue'
export default {
  name: 'MyEditor',
  components: { WangEditor },
  props: {
    text: {
      type: String // 父组件传过来的值
    }
  },
  data() {
    return {
      editor:null
    };
  },
  computed: {},
  mounted() {
    this.createEditor(); // 编辑器初始化
    this.editor.txt.html(this.text); //初始化赋值
  },
  methods: {
    createEditor(){
      const that = this;
      this.editor = new WangEditor('#myeditor')
      this.editor.customConfig.debug = location.href.indexOf('wangeditor_debug_mode=1') > 0;
      // 带格式粘贴
      this.editor.customConfig.pasteFilterStyle = false;
      // 忽略粘贴内容中的图片
      this.editor.customConfig.pasteIgnoreImg = false;
      this.editor.customConfig.customUploadImg = function(files, insert){
        // 图片自定义上传方法
        that.httpUploadImg({ type: 3, file: files[0] })
          .then(res => {
            insert(res); // 光标处插入图片
          },(err) => {
            console.log(err)
          })
      }
      this.editor.customConfig.onchange = (html) => {
        this.info_ = html // 绑定当前值
        this.$emit('change', this.info_) // 将内容同步到父组件中
      }
      this.editor.create()
    }
  },
  watch: {
    text(value) {
      if (value !== this.editor.txt.html()) {
        this.editor.txt.html(value)
      }
    }
  }
};
<style src='@wangeditor/editor/dist/css/style.css'></style>
