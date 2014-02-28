/**
 * A jQuery Function to alert a message based on Twitter Bootstrap Modal
 * 
 * Vivek. V
 * www.vivekv.com 
 * http://blog.vivekv.com/jquery-bootalert-a-simple-bootstrap-alert-function.html
 * 
 * For source and examples, please visit  
 * http://getvivekv.bitbucket.org/BootAlert/
 * 
 * 
 */

$.extend({
	bootalert: function(heading, msg, btnClass) {
		$("#dataAlertModal .modal-footer button").removeClass().addClass("btn").addClass(btnClass);
		if (!$('#dataAlertModal').length) {
			$('body').append('<div id="dataAlertModal" class="modal fade" role="dialog" aria-labelledby="dataAlertLabel" aria-hidden="true"><div class="modal-header"><button type="button" class="close" data-dismiss="modal" aria-hidden="true">&times;</button><h3 id="dataAlertLabel">Notification</h3></div><div class="modal-body"></div><div class="modal-footer"><button class="btn ' + btnClass + '" data-dismiss="modal" aria-hidden="true">Ok</button></div></div>');
		}
			$('#dataAlertModal #dataAlertLabel').text(heading);
			$('#dataAlertModal').find('.modal-body').text(msg);
			$('#dataAlertModal').modal({
				show : true
			});
	}
});