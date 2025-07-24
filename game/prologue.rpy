label prologue:
    scene india_bungalow
    "Penelope Lennox nu a fost niciodată un copil dorit. Sub soarele orbitor al Indiei, trăia ca un obiect uitat într-un sertar - văzută, dar niciodată aleasă."

    show mother

    mother "Las-o pe Ayah să-i dea de mâncare. Am rochia nouă de la Paris de încercat!"

    call relatives_death
    
    scene india_bungalow

    show sheriff
    sheriff "Unchiul tău e un om... particular. Nu te aștepta la flori și îmbrățișări." 
    hide sheriff
    
    show fl
    fl "N-am primit niciodată niciuna. De ce aș începe acum?"
    hide fl
    return

label relatives_death:
    scene india_bungalow_back_yard:
        matrixcolor SaturationMatrix(0)

    "În 48 de ore, tăcerea înghiți totul. Părinții - mumifii în baticuri albe. Ayah - un morman sub cearșaf în curtea din spate. Și Penelope, singură cu un șarpe care-i lingea picioarele goale, așteptând pe cineva... oricine... să-și amintească că există."

    scene india_bungalow_back_yard

    show fl
    fl "Când toți mor, cine rămâne să plângă după tine?"

    hide fl
    return