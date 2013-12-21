
openerp.base_local_modules_menu = function(instance){
    
    instance.web.WebClient.include({
        
        show_annoucement_bar: function() {
            var result = this._super();
            if ( result == undefined || result === false )
            {
                return;
            }
            var $bar = this.$el.find('.announcement_bar');
            var $link = $bar.find('.url a');
            
            result.done(function (){
                $link.attr('href', 'http://openbig.org');
            });
            
        },
        
    });
};