// importei o usestate para conseguir criar e alterar estados
import { useState } from "react";

// importo o css para estilizar o componente
import styles from "./UseStateHook.module.css";

function UseStateHook() {

    // aqui criei o estado contador e começo ele com valor 0
    // no contador guarda o valor
    // esse setcontador serve para alterar esse valor
    const [contador, setContador] = useState(0);

    // isso daq aumenta o contador em 1
    const Aumentar = () => {
        setContador(contador + 1);
    };

    // aq diminui o contador em 1
    const Diminuir = () => {
        setContador(contador - 1);
    };

    // aq volta o contador para 0
    const Zerar = () => {
        setContador(0);
    };

    // aq sorteia um número aleatório entre 0 e 99
    const Sortear = () => {
        setContador(Math.floor(Math.random() * 100));
    };

    return (

        // aq é a div principal do componente
        <div className={styles.container}>

            {/* aq mostra o valor atual do contador */}
            <h1 className={styles.Contador}>{contador}</h1>

            {/* aq chama a função para aumentar */}
            <button className={styles.aumentar} onClick={Aumentar}>+</button>

            {/* aq chama a função para diminuir */}
            <button className={styles.diminuir} onClick={Diminuir}>-</button>

            {/* aq chama a função para zerar */}
            <button className={styles.zerar} onClick={Zerar}>reiniciar</button>

            {/* aq chama a função para sortear um número */}
            <button className={styles.sortear} onClick={Sortear}>sortear</button>

        </div>

    );
}


export default UseStateHook;