function solution(participant, completion) {
const runnerMap = new Map();

    for ( const participant of participants){
        if(!runnerMap.get(participant)){
            runnerMap.set(participant, 1);
        }else{
            runnerMap.set(participant, runnerMap.get(participant)+1);
        }
    }

    for(const completion of completions){
        if(runnerMap.get(completion)){
            runnerMap.set(completion, runnerMap.get(completion)-1);
        }
    }
    
    for(const participant of participants){
        if(runnerMap.get(participant) && runnerMap.get(participant) >=1 ){
            answer = participant;
        }
    }
}
