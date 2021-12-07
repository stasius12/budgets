<template>
  <q-page class="q-pa-xl">
    <q-table
      class="budget-items-table"
      title="Expenses"
      :rows="budget?.budgetitem_set"
      :columns="expensesColumns"
      row-key="name"
      flat
      bordered
    />
  </q-page>
</template>

<script>
import { defineComponent, ref, onMounted } from 'vue';
import { useRoute } from "vue-router";
import { api } from 'boot/axios';

export default defineComponent({
  name: 'Budget',
  setup() {
    const route = useRoute();
    const budget = ref(null);
    const expensesColumns = [
      {
        name: 'expense',
        label: 'Expense',
        field: 'name',
      },
      {
        name: 'value',
        label: 'Value',
        field: 'value',
      },
      {
        name: 'currency',
        label: 'Currency',
        field: 'currency',
      },
      {
        name: 'description',
        label: 'Description',
        field: 'description',
      },
    ]

    const getBudget = async () => {
      try {
        const response = await api.get(`/budgets/budgets/${route.params.id}/`);
        budget.value = response.data;
      } catch (error) {
        console.log(error);
      }
    }

    onMounted(getBudget)

    return {
      budget,
      expensesColumns,
    }

  }
});
</script>

<style lang="scss" scoped>
.budget-items-table {
  height: 310px;

  .q-table__top,
  .q-table__bottom,
  thead tr:first-child th {
    /* bg color is important for th; just specify one */
    background-color: #c1f4cd;
  }

  thead tr th {
    position: sticky;
    z-index: 1;
  }

  thead tr:first-child th {
    top: 0
  }

  /* this is when the loading indicator appears */
  &.q-table--loading thead tr:last-child th {
    /* height of all previous header rows */
    top: 48px
  }
}
</style>
