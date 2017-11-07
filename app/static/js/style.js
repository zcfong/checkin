$(function(){ 
	var pk = '';
	var seat = '';
	var BASEAPI = "";
	var toast = {
		timer: null,
		show: function(msg) {
			var me = this;
			clearTimeout(this.timer);
			$('.toast').remove();
			if(msg) {
				$('body').append('<div class="toast"><span>'+msg+'</span></div>');
			}else {
				$('body').append('<div class="toast"></div>');
			}
			this.timer = setTimeout(function () {
				me.hide();
			},3000);
		},
		hide:function() {
			$('.toast').remove();
			clearTimeout(this.timer);
			this.timer = null;
		}
	};
	// 输入框值发生改变事件
	$('#search-kw').on('input propertychange',function(e){
		pk = '';
		seat = '';
		var value = $(this).val();
		if(value.length>0){
		    var active = $("#activeId").val();
			var url = BASEAPI+'/checkin/query/'+'?t='+Date.now()
			var data = new Object();
			data.active = active;
			data.guest = value;
			$('#search-cross').show();
			$.ajax({
				url: url,
				type: 'GET',
				data: data,
				dataType: 'json',
				crossDomain: true,
				success:function(data){
					if(data.stat == 1 && data.result.length>0){
						var sug = '';
						for(var i = 0;i < data.result.length && i<5; i++){
							sug += '<div class="sug" data-id = "'+data.result[i].pk+'" data-seat="'+data.result[i].seat+'">'+data.result[i].guest+'</div>'
						}
						$('.suggest-content').html(sug);
						$('#search-box').show();
					}
				}
			});
		}else{
			$('#search-cross').hide();
		}
	});
	$('#search-kw').on('focus',function(){
		var top = $(this).offset().top;
		document.body.scrollTop = top;
	});
	// 选择下拉内容事件
	$('#search-box').on('click','.sug',function(){
		var id = $(this).attr('data-id');
		var seatVal = $(this).attr('data-seat');
		pk = id;
		seat = seatVal;
		var value = $(this).text();
		$('#search-kw').val(value);
		$('#search-box').hide();
		$('.seat').text('您的座位是： '+seatVal);
	});
	// 按钮事件
	$('#search-bn').on('click',function(){
		if(pk.length>0){
			var url = BASEAPI+'/checkin/sign/'+pk+'/?t='+Date.now()
			var data = new Object();
			data.pk = pk;
			$.ajax({
				url: url,
				type: 'put',
				data: data,
				dataType: 'json',
				crossDomain: true,
				success:function(data){
					if(data.stat == 1){
						toast.show("签到成功");
						$('.seat').text('您的座位是： '+seat);
					}
				}
			});
		}else{
			toast.show("请输入您的姓名。");
		}
	});
	$('.suggest-close').on('click',function(){
		$('#search-box').hide();
	});
	$('.se-inner .cross').click(function(){
		$('#search-kw').val('');
		$(this).hide();
	});
});





