//
//  Data.swift
//  SideEffect
//
//  Created by Kevin Tran on 10/23/19.
//  Copyright © 2019 Kevin Tran. All rights reserved.
//

import UIKit
import SwiftUI

/*
var threadData: [Thread] = load("threadData.json")

func load<T: Decodable>(_ filename: String, as type: T.Type = T.self) -> T {
    let data: Data
    
    guard let file = Bundle.main.url(forResource: filename, withExtension: nil)
        else {
            fatalError("Couldn't find \(filename) in main bundle.")
    }
    
    do {
        data = try Data(contentsOf: file)
    } catch {
        fatalError("Couldn't load \(filename) from main bundle:\n\(error)")
    }
    
    do {
        let decoder = JSONDecoder()
        return try decoder.decode(T.self, from: data)
    } catch {
        fatalError("Couldn't parse \(filename) as \(T.self):\n\(error)")
    }
}
*/
/*
func add(thread: Thread) {
    do {
        let encoder = JSONEncoder()
        let data = try encoder.encode(thread)
        threadData.append(thread)
        print(threadData)
        print(String(data: data, encoding: .utf8)!)
    } catch {
        fatalError("Couldn't add")
    }
}
*/
