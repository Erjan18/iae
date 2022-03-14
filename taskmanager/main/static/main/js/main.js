$(".burger__icon").on("click", function(){
    $(".burger__line-1").toggleClass("burger__line-1_active");
    $(".burger__line-2").toggleClass("burger__line-2_active");
    $(".burger__line-3").toggleClass("burger__line-3_active");
    // $(".burger__items").toggleClass("is_none");
    $(".burger__items").toggleClass("burger__items-active")
})