<template>
  <v-container class="fill-height">
    <v-responsive class="align-center text-center fill-height">
      <v-img height="300" src="@/assets/logo.svg" />

      <div class="text-body-2 font-weight-light mb-n1">Welcome to</div>

      <h1 class="text-h2 font-weight-bold">OX Quiz</h1>

      <div class="py-14" />

      <v-row class="d-flex align-center justify-center">
        <v-text-field
          v-model="userId"
          class="mx-auto"
          label="User Id"
          min-width="100"
          outlined
          placeholder="Enter your user id"
          prepend-inner-icon="mdi-account"
          type="text"
        ></v-text-field>
      </v-row>

      <v-row class="d-flex align-center justify-center">
        <v-col cols="auto">
          <v-btn
            color="primary"
            min-width="228"
            rel="noopener noreferrer"
            size="x-large"
            variant="flat"
            @click="() => $router.push('/login/' + userId)"
          >
            <v-icon icon="mdi-speedometer" size="large" start />

            Get Started
          </v-btn>
        </v-col>
      </v-row>
    </v-responsive>
  </v-container>
</template>

<script lang="ts" setup>
import { ref } from "vue";

const userId = ref("");
</script>
