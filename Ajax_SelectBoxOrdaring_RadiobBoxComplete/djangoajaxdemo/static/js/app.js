$(function () {
    console.log("Hello!");

    $.ajax({
        url:  '/rooms/list',
        type:  'get',
        dataType:  'json',
        success: function  (data) {
            console.log('data is ',data)
            let rows =  '';
            data.rooms.forEach(room => {
            rows += `
            <tr>
                <td>${room.room_number}</td>
                <td>${room.name}</td>
                <td>${room.nobeds}</td>
                <td>${room.room_type}</td>
                <td>
                    <button class="btn deleteBtn btn-danger" data-id="${room.id}">Delete</button>
                    <button class="btn updateBtn" data-id="${room.id}">Update</button>
                </td>
            </tr>`;
        });
        $('#myTable > tbody').append(rows);


        
        $('.deleteBtn').each((i, elm) => {
            
            $(elm).on("click",  (e) => {
                deleteRoom($(elm))
            })
        })
        }
    });

    function  deleteRoom(el){
        roomId  =  $(el).data('id')
        console.log('room id is : ',roomId)
        $.ajax({
            url:  `/rooms/delete/${roomId}/`,
            type:  'post',
            // dataType:  'json',
            success:  function (data) {
                $(el).parents()[1].remove()
            }
        });
    }

    
    // optional
    $('#sId').on('change', function() {
        var value =$(this).val();
        $.ajax({
          type: "GET",
          url: '/rooms/list',
          data: {
              value: value
          },
          success: function(data){
              console.log("SUCCESS");
             var rows = ''
            data.rooms.forEach(room => {
            rows += `
            <tr>
                <td>${room.room_number}</td>
                <td>${room.name}</td>
                <td>${room.nobeds}</td>
                <td>${room.room_type}</td>
                <td>
                    <button class="btn deleteBtn btn-danger" data-id="${room.id}">Delete</button>
                    <button class="btn updateBtn" data-id="${room.id}">Update</button>
                </td>
            </tr>`;
            
        });
        $('#myTable > tbody').html('')
        $('#myTable > tbody').append(rows);
          },
          failure: function(data){
              console.log("FAIL");
        
          },
      });

    });


    // for Raido
    $("input[name='bed']"). click(function(){
        var radioValue = $("input[name='bed']:checked"). val();
        if(radioValue){
        // alert("Your are a  " + radioValue);
        var checked = $(this).attr('checked', true);
        if(checked){ 
          $(this).attr('checked', false);
        }
        else{ 
          $(this).attr('checked', true);
        }
        $.ajax({
            type: "GET",
            url: '/rooms/list',
            data: {
                value: radioValue
            },
            success: function(data){
                console.log("SUCCESS");
               var rows = ''
              data.rooms.forEach(room => {
              rows += `
              <tr>
                  <td>${room.room_number}</td>
                  <td>${room.name}</td>
                  <td>${room.nobeds}</td>
                  <td>${room.room_type}</td>
                  <td>
                      <button class="btn deleteBtn btn-danger" data-id="${room.id}">Delete</button>
                      <button class="btn updateBtn" data-id="${room.id}">Update</button>
                  </td>
              </tr>`;
              
          });
          $('#myTable > tbody').html('')
          $('#myTable > tbody').append(rows);
            },
            failure: function(data){
                console.log("FAIL");
          
            },
        });





        }
        });
    
});
