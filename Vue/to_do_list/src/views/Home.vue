<template>
  <div class="home">
    <h1 class="title">To Do List</h1>

    <hr>

    <div class="columns">
      <div class="column is-3 is-offset-3">
        <form v-on:submit.prevent="addTask">
          <h2 class="subtitle">Add task</h2>

          <div class="field">
            <label class="label">Title</label>
            <div class="control">
              <input class="input" type="text" v-model="title">
            </div>
          </div>

          <div class="field">
            <label class="label">Details</label>
            <div class="control">
              <input class="input" type="text" v-model="details">
            </div>
          </div>

          <div class="field">
            <label class="label">Status</label>
            <div class="control">
              <div class="select">
                <select v-model="status">
                  <option value="todo">To do</option>
                  <option value="done">Done</option>
                </select>
              </div>
            </div>
          </div>

          <div class="field">
            <div class="control">
              <button class="button is-link">Submit</button>
            </div>
          </div>
        </form>
      </div>
    </div>

    <div class="columns">
      <div class="column is-6" style="margin:auto; width:60%;">
        <h2 class="subtitle">To do</h2>

        <div class="todo">
          <div class="card" v-for="task in tasks" v-bind:key="task.id">
            <div class="card-content" v-if="task.status === 'todo'" v-bind:key="task.id">
              <h2 style="font-size:20px;"><b>{{ task.title }}</b></h2>
              <p>{{ task.details }}</p>
              <p>{{ task.date }}</p>

            </div>

            <footer class="card-footer">
              <a class="card-footer-item" @click="setStatus(task.id, 'done')">Done</a>
            </footer>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
const API_URL = ''
import axios from 'axios'
export default {
  name: 'Home',
  data () {
    return {
      tasks: [],
      title: '',
      status: 'todo'
    }
  },
  mounted () {
    this.getTasks()
  },
  methods: {
    getTasks() {
      axios({
        method: 'get',
        url: 'http://127.0.0.1:8000/todos/',
        auth: {
          username: 'admin',
          password: 'admin'
        }
      }).then(response => this.tasks = response.data)
    },
    addTask() {
      if (this.title) {
        axios({
          method: 'post',
          url: 'http://127.0.0.1:8000/todos/' ,
          data: {
            title: this.title,
            details: this.details,
            date: '2021-08-02T00:15:01Z',
            status: this.status
          },
          auth: {
            username: 'admin',
            password: 'admin'
          }
        }).then((response) => {
          let newTask = {
            'id': response.data.id,
            'details': this.details,
            'date': '2021-08-02T00:15:01Z',
            'title': this.title,
            'status': this.status
          }
          this.tasks.push(newTask)
          this.title = ''
          this.status = 'todo'
        }).catch((error) => {
          console.log(error)
        })
      }
    },
    setStatus(task_id, status) {
      const task = this.tasks.filter(task => task.id === task_id)[0]
      const title = task.title
      axios({
        method: 'put',
        url: 'http://127.0.0.1:8000/todos/',
        headers: {
          'Content-Type': 'application/json',
        },
        data: {
          status: status,
          title: title,
          details: details,
          date: date
        },
        auth: {
          username: 'admin',
          password: 'admin'
        }
      }).then(() => {
        task.status = status
      })
    }
  }
}
</script>

<style lang="scss">
.select, select {
  width: 100%;
}
.card {
  margin-bottom: 20px;
}
.done {
  opacity: 0.3;
}
</style>
