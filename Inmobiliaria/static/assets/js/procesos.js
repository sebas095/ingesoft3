
    var idCaso=0;// pueden cambiar esta variable,, me vale Vrga, luego la validare :v
    $(".AddProceso").click(function(){     
        idCaso=$(this).attr('id');
        console.log("hao");
        $('#agregar_proceso').modal('show');
    });



    $("#GuardarProceso").click(function(e){//al apretar el boton del modal
        console.log("entremadafacka");
        var valido=true;
        $(".requeridoP").each(function(){
            if($(this).val()=="" || $(this).val()=='0'){
                $(this).parent().addClass('has-error');
                valido=false;
            }else{
                $(this).parent().removeClass('has-error');
            }
        });

        if(valido){//si el formulario es válido
            var tipo = $("#Tipo").val();
            var idJuzgado = $("#Juzgado").val();
            var Fv = $("#Fv").val();
            var descripcion = $("#Descripcion").val();

            $('#agregar_proceso').modal('hide');
            //console.log(tipo+"  "+idJuzgado+"  "+ Fv+"  "+descripcion);

            $.ajax({
                url: "{% url 'CrearProceso' %}",
                type: 'POST',
                async: true,
                data: { caso : idCaso, 
                        tipo : tipo,
                        descripcion : descripcion,
                        juzgado : idJuzgado,
                        fecha_vencimiento : Fv,
                    },
                success: function(resp){
                    if(resp.message == '1'){
                        $(".iproceso").each(function(){
                            $(this).val(''); 
                        });
                        $("#Juzgado").val('0')

                        $('#mensaje_exito').modal('show').one('click', '#aceptar', function () {
                            $('#Proceso'+idCaso).load("/proceso_ver/"+idCaso);
                        });;

                    }else{
                        if(resp.message == '2'){
                            alert("2");
                        }else{
                            for(var index in resp.message){
                                $('#error').html(resp.message[index]);
                            }
                            $('#mensaje_existe').modal('show');
                        }
                    }
                },
                error: function(jqXHR,estado,error){
                    alert("Error: "+error+"     Estado: "+estado);
                },
                 
            });
        }

    });
