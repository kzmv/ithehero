$(document).ready(function(){
    $('.nav-item').click(function(e) {
        $('.nav-item.active').removeClass('active');
        var $this = $(this);
        if (!$this.hasClass('active')) {
            $this.addClass('active');
        }
    });
});
