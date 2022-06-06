<template>
  <el-row >
    <nav class="navbar navbar-expand-lg navbar-light bg-light" >
      <a class="navbar-brand" href="#">Compose a Message</a>
    </nav>
    <v-jsoneditor v-model="content" :options="options"></v-jsoneditor>
    <div style="text-align: center">
      <el-button type="secondary" @click="send">Send</el-button>
    </div>

    <message-list v-bind:messages="recent_messages" style="padding-right: 20px;padding-left: 20px"></message-list>
  </el-row>
</template>

<script>
import VJsoneditor from 'v-jsoneditor';
import message_bus from '@/message_bus.js';
import MessageList from '../MessageHistory/MessageList.vue';
import share from '@/share.js';

export const metadata = {
  menu: {
    label: 'Compose',
    icon: 'el-icon-message',
    group: 'Debug',
    priority: 40,
    required_protocols: [
    ]
  }
};

export default {
  name: 'compose',
  mixins: [
    message_bus(),
    share({
      use: ['message_history']
    })
  ],
  components: {
    VJsoneditor,
    MessageList
  },
  data: function() {
    return {
      content: {
        "@type": "did:sov:BzCbsNYhMrjHiqZDTUASHg;spec/trust_ping/1.0/ping",
        "response_requested": true
      },
      options: {
        "mode": "code"
      }
    };
  },
  computed: {
    recent_messages: function() {
      return this.message_history.slice(-5)
    }
  },
  methods: {
    send: function() {
      this.send_message(this.content);
    }
  }
}
</script>
