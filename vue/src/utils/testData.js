// LocalStorage keys
export const TOKEN_OBJECT_KEY = "TokenObject";
export const TOKEN_KEY = "Token";
export const u="http://127.0.0.1:80";
// 站点相关信息
export const yonghu = {
    userName:'',
    password:'',
    permission:'',
	id:''
};
export const comic = {
    comic:{
		id:'',
		comicName:'',
		cover:'',
		description:'',
		label:'',
		nickName:'',
		number:'',
		popularity:'',
		region:'',
		remark:'',
		updateTime:'',
		year:''
	},
    
};
// SideBar 测试数据
export const permission = [
	
	{
		title: "管理员",
		path: "/permission",
		icon: "el-icon-user-solid",
		subItems: [
			{
				title: "用户管理",
				path: "/permission/user",
			},
			{
				title: "动漫管理",
				path: "/permission/comic"
			},
		],
	}
	
	
];

