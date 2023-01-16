<template>
<b-overlay rounded="sm" :show="logado">
        <b-form>
        <b-form-group label="Usuário:"
            :state=userOK :invalid-feedback=userInvalido>
            <b-input-group>
                <b-input-group-prepend is-text>
                    <b-icon-person></b-icon-person>
                </b-input-group-prepend>
                <b-form-input id='email'
                    type="text"
                    placeholder="Usuario" v-model="user.email">
                </b-form-input>
            </b-input-group>
        </b-form-group>
        <b-form-group label="Senha:" :state=senhaOK :invalid-feedback=senhaInvalida>
            <b-input-group>
                <b-input-group-prepend is-text>
                    <b-icon-key></b-icon-key>
                </b-input-group-prepend>
                <b-form-input id='senha'
                    :type=senhaType
                    placeholder="Senha" v-model="user.password">
                </b-form-input>
                <b-button  @mousedown="mostraSenha" :variant=senhaClass> <b-icon icon='brightness-alt-high'></b-icon> </b-button>
            </b-input-group>
        </b-form-group>
        <b-alert
            variant="warning"
            dismissible
            fade
            :show="loginFalha"
            @dismissed="showDismissibleAlert=false">
                Usuário ou Senha Incorreto(s)!
        </b-alert>
        <b-alert
            variant="danger"
            dismissible
            fade
            :show="erro"
            @dismissed="showDismissibleAlert=false">
                falha no servidor {{erroDetalhes}}
        </b-alert>
        <b-form-group class="mt-3 pt-3">
            <b-button @click="chamaLogin" v-bind:class="{disabled:!podelogar}"  block variant="primary">
                <span v-show="espera">
                <b-spinner type="grow" variant="light"></b-spinner>
                <b-spinner type="grow" variant="light"></b-spinner>
                <b-spinner type="grow" variant="light"></b-spinner>
               </span>
               <span v-show="!espera">Login</span>
            </b-button>
        </b-form-group>
    </b-form>
        <template #overlay>
            <div class="text-center">
                <b-icon icon="check-circle" animation="throb" font-scale="5" variant="success"></b-icon>
            </div>
        </template>
    </b-overlay>    
</template>

<script>
export default {
    data(){
        return{
            erroDetalhes:'',
            erro:false,
            logado:false,
            loginFalha: false,
            espera:false,
            senhaType:'password',
            senhaClass:'dark',
            senhaShow: true,
            user:{
                email: '',
                password: '',
                csrfmiddlewaretoken: this.getCookie('csrftoken')
            }
        }
    },
    props:{
        caminho: String,
    },
    computed:{
        userOK(){
            var valor = this.user.email.length
            return valor>0 && this.user.email.indexOf(' ')<0 
        },
        userInvalido(){
            var valor = this.user.email.length
            if(valor<=0){return "Campo Obrigatorio"}
            else if(this.user.email.indexOf(' ')>0){return "espaço não é permitido"}
            else{return 'ok'}
        },
        senhaOK(){
            return this.user.password.length>0
        },
        senhaInvalida(){
            if(this.user.password.length<=0){
                return "senha Necessária!"
            }else{
                return "ok"
            }
        },
        podelogar(){
            return this.userOK && this.senhaOK
        }
    },
    methods:{
        chamaLogin(){
            this.loginFalha=false;
            if(this.podelogar){
                this.espera = true
                //this.login()
                //this.csfrGet()
                }
        },
        async login() {
            this.user.csrfmiddlewaretoken = this.getCookie('csrftoken')
            fetch(`${this.$host}${this.caminho}`,{
                    method: 'post',
                    credentials:'include',
                    headers:{
                        'Access-Control-Allow-Credentials': true
                    },
                    body: JSON.stringify(this.user)
            }).then(res=>{
                if(res.status === 200){
                    return res.text()
                }else if(res.status===400) {
                    this.loginFalha=true
                    this.espera=false
                }else{
                    this.erro = true
                    this.espera=false
                    throw 'Erro - servidor fora do ar '
                }
            }).then(result=>{
                    if(result.indexOf('ok')>=0){
                        this.logado = true
                        console.log(result)
                        this.$emit('logou',true)
                    }else if(result=="usuario"){
                        this.loginFalha=true
                        this.espera=false
                    }else{
                        this.erro = true
                        this.espera=false
                        throw "Erro no servidor - ",this.result
                    }  
            }).catch(erro=>{
                this.erroDetalhes = `--- ${erro}`
                this.erro = true
                this.espera=false
                console.log(erro)
            })
       },
        async csfrGet() {
            fetch(`${this.$host}/user/login/`,{
                    method: 'get',
            }).then(res=>{
                if(res.status === 200){
                    return res.text()
                }else if(res.status===400) {
                    this.loginFalha=true
                    this.espera=false
                }else{
                    this.erro = true
                    this.espera=false
                    throw 'Erro - servidor fora do ar '
                }
            }).then(result=>{
                    if(result != undefined){
                        this.setCookie("csrftoken",result)
                        this.login()
                    }else if(result=="usuario"){
                        this.loginFalha=true
                        this.espera=false
                    }else{
                        this.erro = true
                        this.espera=false
                        throw 'Erro no servidor'
                    }  
            }).catch(erro=>{
                this.erroDetalhes = `--- ${erro}`
                this.erro = true
                this.espera=false
                console.log(erro)
            })
       },
       mostraSenha: function(){
           if(this.senhaShow==true){
               this.senhaShow = false;
               this.senhaClass = 'light';
               this.senhaType = 'text';
           }else{
               this.senhaShow = true;
               this.senhaClass = 'dark';
               this.senhaType = 'password';
           }
       }
    }
}
</script>