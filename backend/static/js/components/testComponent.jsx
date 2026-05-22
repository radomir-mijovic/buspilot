import { useState } from "react"

export default function TestComponent() {
    const [number, setNumber] = useState(0)
    return (
        <div>
            <button onClick={() => setNumber(prevState => prevState + 1)}>Increse</button>
            <h4>{number}</h4>
            <button onClick={() => setNumber(prevState => prevState - 1)}>Decrese</button>
        </div>
    )
}
