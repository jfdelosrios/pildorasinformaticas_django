from gestionPedidos.forms import FormularioContacto

miFormulario=FormularioContacto()
#print(miFormulario) #formato tabla
#print(miFormulario.as_p()) #formato parrafo
#print(miFormulario.as_ul()) #formato lista

miFormulario=FormularioContacto({'asunto':'prueba','email':'jfdelosrios@hotmail.com','mensaje':'mensaje de prueba'})
print(miFormulario.is_valid())
print(miFormulario.cleaned_data)