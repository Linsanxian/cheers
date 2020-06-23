<template>
  <div class="home">
    <hello-world/>
  </div>
</template>

<script>
    import HelloWorld from "@/components/HelloWorld.vue";

    export default {
        name: "home",
        components: {
            HelloWorld
        }
    };
</script>
