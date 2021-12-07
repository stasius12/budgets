<template>
  <q-page class="flex flex-center q-px-xl">
    <q-card v-for="budget in budgets" :key="budget?.id" class="budget-card q-ma-xl">
      <q-card-section>
        <div class="text-h6">{{ budget.name }}</div>
        <div class="text-subtitle2">by John Doe</div>
      </q-card-section>

      <q-card-section>
        {{ budget?.description || '' }}
      </q-card-section>

      <q-separator />

      <q-card-actions vertical>
        <q-btn flat @click="$router.push({name: 'budget', params: {id: budget.id}})"><i class="far fa-eye q-mr-sm"></i> Open</q-btn>
        <q-btn flat color="blue"><i class="fas fa-share-alt q-mr-sm"></i> Share</q-btn>
        <q-btn flat color="red" @click="removeBudget(budget.id)"><i class="fas fa-trash-alt q-mr-sm"></i> Remove</q-btn>
      </q-card-actions>
    </q-card>
    <q-card>
      <q-btn @click="newBudgetPrompt = true"><i class="fas fa-plus q-mr-sm"></i> Add new budget</q-btn>
    </q-card>

    <q-dialog v-model="newBudgetPrompt" persistent>
      <q-card style="min-width: 350px">
        <q-card-section>
          <div class="text-h6">Add new budget</div>
        </q-card-section>

        <q-form>
          <q-card-section class="q-pt-none">
            <q-input v-model="newBudgetTitle" type="text" label="Title" :rules="[(val) => !!val || 'You must enter a title']" dense autofocus @keyup.enter="newBudgetPrompt = false" />
            <q-input v-model="newBudgetDescription" type="textarea" label="Description" dense autofocus @keyup.enter="newBudgetPrompt = false" />
          </q-card-section>

          <q-card-actions align="right" class="text-primary">
            <q-btn v-close-popup flat label="Cancel" />
            <q-btn flat label="Add budget" @click="createBudget" />
          </q-card-actions>
        </q-form>
      </q-card>
    </q-dialog>
  </q-page>
</template>

<script>
import { defineComponent, ref, onMounted } from 'vue';
import { api } from 'boot/axios';

export default defineComponent({
  name: 'PageIndex',
  setup() {
    const budgets = ref([]);

    const newBudgetPrompt = ref(false);
    const newBudgetTitle = ref("");
    const newBudgetDescription = ref("");

    const getBudgets = async () => {
      try {
        const response = await api.get("/budgets/budgets/");
        budgets.value = response.data;
      } catch (error) {
        console.log(error);
      }
    }

    const createBudget = async () => {
      if (!newBudgetTitle.value) return;

      try {
        await api.post(
          "/budgets/budgets/",
          {name: newBudgetTitle.value, description: newBudgetDescription.value, user: 1},
        );

        newBudgetPrompt.value = false;
        newBudgetTitle.value = "";
        newBudgetDescription.value = "";

        await getBudgets();

      } catch (error) {
        console.log(error);
      }
    }

    const removeBudget = async (budgetID) => {
      try {
        await api.delete(`/budgets/budgets/${budgetID}/`);

        await getBudgets();

      } catch (error) {
        console.log(error);
      }
    }

    onMounted(getBudgets);

    return {
      budgets,
      createBudget,
      removeBudget,
      newBudgetPrompt,
      newBudgetTitle,
      newBudgetDescription,
    }
  }
})
</script>

<style lang="scss" scoped>
.budget-card {
  width: 300px;
}
</style>
