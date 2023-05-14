<template>
    <!-- 动漫修改 -->
	<el-dialog title="编辑动漫" :visible.sync="dialogData.showEditDialog" width="600px" @close="cancelForm">
		<!--
			表单校验
				el-form 标签加上 ref、:model、:rules
				el-form-item 标签设置对应的 prop 属性
				props || data 设置对应的模型
		-->
		<el-form
			ref="model"
			:model="model"
			:rules="rules"
			:label-position="labelPosition"
			:label-width="formLabelWidth"
		>
			<el-form-item label="动漫名：" prop="comicName">
				<el-input v-model="model.comicName" class="zuo"></el-input>
			</el-form-item>
            <el-form-item label="昵称：" prop="nickName">
				<el-input v-model="model.nickname" class="zuo"></el-input>
			</el-form-item>
			<!-- <el-form-item label="日期" prop="occurDate">
				<el-date-picker
					v-model="model.occurDate"
					type="datetime"
					placeholder="选择日期时间"
					value-format="yyyy-MM-dd HH:mm:SS"
				></el-date-picker>
			</el-form-item> -->

			<el-form-item label="封面：">
				<el-upload
					:action="fileUploadInfo.action"
					:headers="fileUploadInfo.headers"
					list-type="picture-card"
					:on-preview="handlePictureCardPreview"
					:on-remove="handleRemove"
					:on-success="handleSuccess"
					:before-upload="beforeUpload"
					:file-list="comicimg"
					name="image"
				>
					<i class="el-icon-plus"></i>
				</el-upload>

				<el-dialog :visible.sync="dialogVisible">
					<img width="100%" :src="dialogImageUrl" alt="" />
				</el-dialog>
			</el-form-item>


            <el-form-item label="地区：" prop="region">
				<el-input v-model="model.region" class="zuo"></el-input>
			</el-form-item>
            <el-form-item label="标签：" prop="label">
				<el-input v-model="model.label" class="zuo"></el-input>
			</el-form-item>
            <el-form-item label="简介：" prop="description">
				<el-input v-model="model.description" class="zuo"></el-input>
			</el-form-item>
            <el-form-item label="更新情况：" prop="remark">
				<el-input v-model="model.remark" class="zuo"></el-input>
			</el-form-item>
            <el-form-item label="上映年：" prop="year">
				<el-input v-model="model.year" class="zuo"></el-input>
			</el-form-item>
            <el-form-item label="更新时间：" prop="updateTime">
				<el-input v-model="model.updateTime" class="zuo"></el-input>
			</el-form-item>
            <el-form-item label="章节数：" prop="number">
				<el-input v-model="model.number" class="zuo"></el-input>
			</el-form-item>
            <el-form-item label="人气：" prop="popularity">
				<el-input v-model="model.popularity" class="zuo"></el-input>
			</el-form-item>
            <el-form-item label="链接：" prop="url">
				<el-input v-model="model.url" class="zuo"></el-input>
			</el-form-item>
		</el-form>

		<div slot="footer" class="dialog-footer">
			<el-button @click="cancelForm()">取 消</el-button>
			<el-button type="primary" @click="submitForm()">确 定</el-button>
		</div>
	</el-dialog>
</template>

<script>
import { u } from '@/utils/testData';



export default {
	name: "ComicEdit",
	props: {
		dialogData: {
			type: Object,
			default: {
				id: 0,
				showEditDialog: false,
			},
		},
	},
	data: function () {
		return {
			// 弹出框设置项
			formLabelWidth: "80px",
			labelPosition: "right",
			model: {
				id: 0,
				comicName: "",
				nickname: "",
				cover: "",
                region:"",
                label:"",
                description:"",
                remark:"",
                year:"",
                updateTime:"",
                number:"",
                popularity:""
			},
			rules: {
				comicName: [
					{
						required: true,
						message: "动漫名不能为空",
						trigger: ["blur", "change"],
					},
				],
				nickname: [
					{
						required: true,
						message: "昵称不能为空",
						trigger: ["blur", "change"],
					},
				],
        
			},
			comicimg:[{
				url:'',
				},
			],
			// 用户相关
			// user: this.$Storage.getItemForLs(this.$TestData.TOKEN_OBJECT_KEY),
			// 上传图片设置
			dialogImageUrl: "",
			dialogVisible: false,
			fileUploadInfo: {
				action: this.$Request.domain + "/upload",
				// headers: {
				// 	Token: this.$Storage.getItemForLs(this.$TestData.TOKEN_KEY),
				// },
			},
		};
	},
	methods: {
		// 上传图片相关方法
		handleRemove(file, fileList) {},
		handlePictureCardPreview(file) {
			this.dialogImageUrl = this.$Request.domain + file.url;
			this.dialogVisible = true;
		},
		beforeUpload: function (file) {
			const isJPG = file.type === "image/jpeg";
			const isLt4M = file.size / 1024 / 1024 < 4;
			// if (!isJPG) {
			// 	this.$message.error("上传头像图片只能是 JPG 格式!");
			// }
			if (!isLt4M) {
				this.$message.error("上传头像图片大小不能超过 4 MB!");
			}
			return isLt4M;
		},
		handleSuccess: function (response, image, fileList) {
			console.log(response)
			if (response.code == 200) {
				var image = {};
				image.url = this.$Request.domain + response.data;
				image.src = this.$Request.domain + response.data;
				this.model.cover = response.data;
			} else {
				this.$message.error("上传图片失败");
			}
		},
		// 取消
		cancelForm: function () {
			this.dialogData.showEditDialog = false;
		},
		// 提交表单
		submitForm: function () {
			// 验证表单并提交 Model
			this.$refs["model"].validate((isValid) => {
				if (!isValid) return;
                console.log(this.model)
                    var type = "post";
                    this.$Request
					.fetch_("/addcomic", type, this.model) //添加   传入comic数据
					.then((result) => {
						console.log(result)
						if (result == 200) {
							this.$message.info("上传成功");
							this.$emit("emitDialogData", false);
						} else {
							this.$message.info(result.message);
						}
					})
					.catch((error) => {
						this.$message.error("提交出错。");
					});
                

				// this.$Request
				// 	.fetch_("/comic/update", type, this.model) //修改   传入comic数据
				// 	.then((result) => {
				// 		if (result.code == this.$Request.OK_CODE) {
				// 			this.$refs["model"].resetFields();
				// 			this.$emit("emitDialogData", false);
				// 		} else {
				// 			this.$message.info(result.message);
				// 		}
				// 	})
				// 	.catch((error) => {
				// 		this.$message.error("提交出错。");
				// 	});
			});
		},
		// 改变富文本框事件
		change(val) {},
	},
	watch: {
		// 监听 dialogData.id，初始化模型
		dialogData: function (newVal, oldVal) {
			if (newVal.id == 0) {
				if (typeof this.$refs["model"] != "undefined") {
					// 重置 model
					this.model = {
						id: 0,
						comicName: "",
						nickname: "",
						cover: "",
                        region:"",
                        label:"",
                        description:"",
                        remark:"",
                        year:"",
                        updateTime:"",
                        number:"",
                        popularity:""
					};
					this.$refs["model"].resetFields();
				}
			} else {
				var url = "/findById?id=" + this.dialogData.id; //根据id查comic
				this.$Request
					.fetch(url)
					.then((result) => {
						this.model = result.data[0];
						this.comicimg[0].url=this.$Request.domain + this.model.cover;
						console.log(this.comicimg)
					})
					.catch((error) => {
					
					});
			}
		},
	},
	mounted: function () {},
};
</script>

<style scoped>
 .el-select,
.zuo {
	width: 300px;
	float: left;
} 
</style>
