<template>
	<div id="app">
		<item-image />
		<item-title />
		<item-description />
	</div>
</template>

<script>
import ItemImage from './components/ItemImage.vue'
import ItemDescription from './components/ItemDescription.vue'
import ItemTitle from './components/ItemTitle.vue'
export default {

  name: 'App',

  components: {
  	ItemTitle,
  	ItemImage,
  	ItemDescription
  }
};
</script>

<style lang="css" scoped>
</style>										