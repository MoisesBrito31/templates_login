<template>
<div>
    <b-overlay rounded="sm" :show="!loadFim">
        <div class="card">
            <div class="card-header row">
                <div class="card-title form-inline col">
                    <h2>Item.nome</h2>                
                </div>
                <div class="text-right col">
                        <b-button  variant="light">
                        <b-icon icon="pencil" variant="dark"></b-icon>
                    </b-button>
                </div>
            </div>
            <div class="card-body">
                <div class="row">
                    <div class="col-auto m-auto pb-5">
                        <b-img></b-img>
                    </div>
                    <div class="col-6 pb-5" style="min-width: 350px;">
                        <div class="form-group">
                            <label><strong><h5> Descriçao:</h5></strong></label>
                            <p>
                                Item.descricao
                            </p>
                        </div>
                        <div class="row mt-5">
                            <div class="col">
                                <div class="form-group">
                                    <label><strong><h5>Fabricante:</h5></strong></label>
                                    <p>Item.fabricante</p>
                                </div>
                            </div>
                            <div class="col">
                                <div class="form-group">
                                    <label><strong><h5>Linha:</h5></strong></label>
                                    <p>Item.linha</p>
                                </div>
                            </div>
                            <div class="col">
                                <div class="form-group">
                                    <label><strong><h5>Tipo:</h5></strong></label>
                                    <p>Item.tipo</p>
                                </div>
                            </div>
                            <div class="col">
                                <div class="form-group">
                                    <label><strong><h5>Familia:</h5></strong></label>
                                    <p>Item.familia</p>
                                </div>
                            </div>
                            <div class="col">
                                <div class="form-group">
                                    <label><strong><h5>Preço:</h5></strong></label>
                                    <p>R$   Item.preco</p>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
        <template #overlay>
            <div class="text-center">
                <div v-if="erro">
                    <b-icon icon="x-circle" animation="throb" font-scale="4" ></b-icon>
                    <p class="text-danger">{{erroDetalhes}}</p>
                </div>
                <div v-else>
                    <b-icon icon="arrow-clockwise" animation="spin" font-scale="4"></b-icon>
                </div>
            </div>
        </template>
    </b-overlay>
</div>
</template>
<script>
export default {
    name:'userView',
    data(){
        return{
            loadFim:false,
            erroDetalhes:'',
            erro:false,
        }
    },
    created(){
        this.load()
    },
    methods:{
        load(){
            this.getData()
        },
        async getData(){
            fetch(`${this.$host}/user/view/`,{
                    method: 'get',
                    credentials:'include',
            }).then(res=>{
                if(res.status === 200){
                    return res.text()
                }else if(res.status===400) {
                    this.erro = true
                    this.loadFim= true
                }else{
                    this.erro = true
                    this.loadFim=true
                    throw 'Erro - servidor fora do ar '
                }
            }).then(result=>{
                    if(result.indexOf('falha')<0){
                        var data = result.split(',')
                        console.log(data)
                        this.loadFim=true
                        this.erro=false
                    }else{
                        this.erro = true
                        this.loadFim=true
                        throw 'Erro no servidor'
                    }  
            }).catch(erro=>{
                this.erroDetalhes = `--- ${erro}`
                this.erro = true
                this.espera=false
                console.log(erro)
            })
        },
    },
}
</script>