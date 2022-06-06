<template >

  <el-row>
      <el-dialog
        title="Scan Invitation"
        :visible.sync="QRDialogVisible"
        width="500">
        <div style="margin-left:auto;margin-right:auto;">
          <qrcode v-bind:value="QRDialogURL" :options="{ width: 400 }"></qrcode>
        </div>
      </el-dialog>

      <el-row class="navbar navbar-expand-lg navbar-light bg-light" justify="end">
        <el-col :span="22"><a class="navbar-brand" href="#">Invitations</a></el-col>
        <el-col :span="2">
          <el-button
            type="primary"
            icon="el-icon-refresh"
            @click="fetch_invitations_v1"></el-button>
        </el-col>
      </el-row>

      <el-collapse v-model="expanded_items" style="width: 100%">
        <ul class="list">
          <el-collapse-item
            v-for="i in invitations_v1"
            v-bind:title="'\xa0\xa0\xa0\xa0\xa0'+get_name(i)"
            :name="get_name(i)"
            :key="i.id">
            <el-row :key="i.id" style="padding-left: 20px">
              <ul>
                <li><strong>Auto Accept:</strong> {{i.auto_accept}}</li>
                <li><strong>Multi-use:</strong> {{i.multi_use}}</li>
                <li><strong>Created:</strong> {{i.created_date}}</li>
              </ul>
              <div style="text-align: center">
                <el-button type="primary" @click="copyURL(i.invitation_url)">Copy URL</el-button>
                <el-button type="primary" @click="presentQR(i.invitation_url)">Scan QR</el-button>
              </div>
              <div>
                <vue-json-pretty
                  :deep=0
                  :data="i">
                </vue-json-pretty>
              </div>
            </el-row>
          </el-collapse-item>
        </ul>
      </el-collapse>

  <!--    <el-divider></el-divider>-->


      <p class="navbar navbar-expand-lg navbar-light">Create Invitations:</p>
      <el-form :inline="false" label-width="120px">
        <el-form-item label="Alias:">
          <el-input v-model="invite_form.alias" style="width:200px;"> </el-input>
          <i>Alias used in your list of invitations.</i>
        </el-form-item>
        <el-form-item label="Label:">
          <el-input v-model="invite_form.label" style="width:200px;"> </el-input>
          <i>The label is presented in the invitation to the recipient.</i>
        </el-form-item>
        <el-form-item label="Group:">
          <el-input v-model="invite_form.group" style="width:200px;"> </el-input>
          <i>The group assigned to new connections that use this invitation</i>
        </el-form-item>
        <el-form-item v-if="supports_mediation" label="Mediator:">
          <el-select style="width: 200px;"
                     v-model="invite_form.mediation_id"
                     filterable
                     no-data-text="No mediators found"
                     placeholder="Mediator">
            <el-option
              v-for="mediator in mediators"
              :key="mediator.mediation_id"
              :label="mediator_name(mediator)"
              :value="mediator.mediation_id">
            </el-option>
          </el-select>
          <i>Optionally select a mediator for this invitation.</i>
        </el-form-item>
        <el-form-item label="Auto Accept:">
          <el-switch v-model="invite_form.auto_accept"></el-switch>
          <i>Auto accepted invitations will automatically respond to connection requests.</i>
        </el-form-item>
        <el-form-item label="Multi Use:">
          <el-switch v-model="invite_form.multi_use"></el-switch>
          <i>Multi-use invitations can be used more than onece. </i>
        </el-form-item>
        <el-form-item>
          <el-col :span="2" :offset="19">
            <el-button type="primary" icon="el-icon-check" @click="fetchNewInvite()">Create</el-button>
          </el-col>
        </el-form-item>
      </el-form>



  </el-row>
</template>

<script>
import VueJsonPretty from 'vue-json-pretty';
const { clipboard } = require('electron');
import VueQrcode from '@chenfengyuan/vue-qrcode';
import message_bus from '@/message_bus.js';
import share from '@/share.js';
import { COORDINATE_MEDIATION } from '../Mediator';

export const metadata = {
  menu: {
    label: 'Invitations',
    icon: 'el-icon-plus',
    group: 'Connection',
    priority: 10,
    required_protocols: [
      'https://github.com/hyperledger/aries-toolbox/tree/master/docs/admin-invitations/0.1'
    ]
  }
};
// elements here need to be unique
export const shared = {
  data: {
    invitations_v1: [],
  },
  listeners: {
    'https://github.com/hyperledger/aries-toolbox/tree/master/docs/admin-invitations/0.1/list': (share, msg) => {
      share.invitations_v1 = msg.results;
    }
  },
  methods: {
    fetch_invitations_v1: ({send}) => {
      send({
        "@type": "https://github.com/hyperledger/aries-toolbox/tree/master/docs/admin-invitations/0.1/get-list",
      });
    }
  }
}

export default {
  name: 'invitations_new',
  mixins: [
    message_bus({events: {
      'https://github.com/hyperledger/aries-toolbox/tree/master/docs/admin-invitations/0.1/invitation': (v, msg) => {
        v.fetch_invitations_v1()
      }
    }}),
    share({
      use: ['invitations_v1', 'protocols', 'mediators', 'active_connections'],
      actions: ['fetch_invitations_v1', 'fetch_mediators', 'fetch_connections']
    })
  ],
  components: {
    VueJsonPretty,
    'qrcode': VueQrcode
  },
  data () {
    return {
      expanded_items: [],
      QRDialogVisible: false,
      QRDialogURL: '',
      invite_form: {
        label: "",
        alias: "",
        group: "",
        mediation_id: "",
        auto_accept: true,
        multi_use: false,
      }
    }
  },
  computed: {
    supports_mediation: function() {
      let list = this.protocols.map(p => p.pid);
      return list.includes(COORDINATE_MEDIATION)
    },
  },
  created: async function() {
    await this.ready();
    this.fetch_invitations_v1();
    if (this.supports_mediation) {
      this.fetch_connections();
      this.fetch_mediators();
    }
  },
  methods: {
    async fetchNewInvite(){
      let query_msg = {
        "@type": "https://github.com/hyperledger/aries-toolbox/tree/master/docs/admin-invitations/0.1/create",
        ...this.invite_form
      };
      this.invite_form.label = "";
      this.invite_form.alias = "";
      this.invite_form.group = "";
      this.invite_form.mediation_id = "";
      this.invite_form.auto_accept = true;
      this.invite_form.multi_use = false;
      this.send_message(query_msg);
    },
    get_name: function(i) {
      if(i.alias){
        return i.alias;
      }
      return `${i.multi_use ? "Multi-use: " : ""}${i.label}, created ${i.raw_repr.connection.created_at}`;
    },
    copyURL: function(url){
      clipboard.writeText(url);
      this.$notify({
          type: 'success',
          title: 'Copied',
          message: 'This Invitation has been copied to the clipboard.',
          duration: 2000
        });
    },
    presentQR: function(url){
      this.QRDialogURL = url;
      this.QRDialogVisible = true;
    },
    mediator_name: function(mediator) {
      let connection_label = 'Unknown';
      let matched_connection = this.active_connections.filter(
        c => c.connection_id == mediator.connection_id
      );
      if(matched_connection.length == 1){
        connection_label = matched_connection[0].label;
      }
      return connection_label;
    },
  }
}
</script>
