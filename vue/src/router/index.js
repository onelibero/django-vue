import Vue from "vue";
import Router from "vue-router";

Vue.use(Router);

export default new Router({
	mode: "history", // history 模式去除地址栏 # 号
	routes: [
		{
			// http://127.0.0.1:8080/login
			path: "/login",
			name: "登录",
			component: () => import("@/components/login.vue"),
			meta: { requireAuth: false },
		},
		{
			// http://127.0.0.1:8080/
			path: "/",
			name: "主页",
			component: () => import("@/components/Index.vue"),
            meta: { requireAuth: false },
		},
		{
			// http://127.0.0.1:8080/account
			path: "/detail",
			name: "动漫详情",
			component: () => import("@/components/ComicDetail.vue"),
            meta: { requireAuth: true },
		},
		{
			// http://127.0.0.1:8080/test
			path: "/permission",
			name: "管理员",
			component: () => import("@/components/Permission.vue"),
			redirect: "/permission/user",
			// 二级路由，渲染到该组件中的 <router-vi@/components/User/Update.vue
			children: [
				{
					// http://127.0.0.1:8080/test/helloworld1
					path: "/permission/user",
					name: "用户管理",
					component: () => import("@/components/User.vue"),
					meta: { requireAuth: true}
				},
				{
					// http://127.0.0.1:8080/test/helloworld2
					path: "/permission/comic",
					name: "动漫管理",
					component: () => import("@/components/Comic.vue"),
					meta: { requireAuth: true },
				},
				
			],
		},
	],
});
