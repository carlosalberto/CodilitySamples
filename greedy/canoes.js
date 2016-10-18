
function solution(A, K) {
    var n = A.length;
    var lastIdx = n - 1;

    var skinny = [];
    var fatso = [];
    var canoes = 0;

    for (var i = 0; i < n - 1; i++) {
        if (A[i] + A[lastIdx] <= K)
            skinny.push(A[i]);
        else
            fatso.push(A[i]);
    }
    fatso.push(A[lastIdx]);

    while (fatso.length > 0) {
        if (skinny.length > 0) skinny.pop();
        fatso.pop();

        canoes++;

        if (fatso.length == 0 && skinny.length > 0)
            fatso.push(skinny.pop());

        while (fatso.length > 1 && fatso[0] + fatso[fatso.length - 1] <= K)
            skinny.push(fatso.shift());
    }

    return canoes;
}

console.log(solution([13, 14, 17, 21, 33, 35], 35));
console.log(solution([ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 ], 10));

