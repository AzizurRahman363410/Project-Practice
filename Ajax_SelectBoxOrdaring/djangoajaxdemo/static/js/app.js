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
                    <button class="btn deleteBtn" data-id="${room.id}">Delete</button>
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
                    <button class="btn deleteBtn" data-id="${room.id}">Delete</button>
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
    
});
