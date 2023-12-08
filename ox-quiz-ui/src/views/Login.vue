<template>
  <v-container>
    <v-row>
      <input v-model="sendMsg" />
      <button @click="send">Send</button>
      <input v-model="receivedMsg" />
    </v-row>
  </v-container>
</template>

<script lang="ts" setup>
import { ref } from "vue";

const props = defineProps({
  userId: {
    type: String,
    required: true,
  },
});

const sendMsg = ref("");
const receivedMsg = ref("");

console.log("userId", props.userId);

const ws = ref(new WebSocket("ws://localhost:8000/ws/" + props.userId));

const send = () => {
  console.log("send", sendMsg.value);
  ws.value.send(sendMsg.value);
};

ws.value.onmessage = (event) => {
  console.log("received", event.data);
  receivedMsg.value = event.data;
};

ws.value.onopen = () => {
  console.log("connected");
};

ws.value.onclose = () => {
  console.log("disconnected");
};

ws.value.onerror = (err) => {
  console.error(err);
};
</script>
