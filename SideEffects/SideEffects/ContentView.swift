//
//  ContentView.swift
//  SideEffects
//
//  Created by Kevin Tran on 11/15/19.
//  Copyright © 2019 Kevin Tran. All rights reserved.
//

import SwiftUI

struct ContentView: View {
    var body: some View {
        VStack(alignment: .leading) {
            NavigationView {
                VStack {
                    Image("logo")
                        .resizable()
                        .frame(width: 200.0, height: 200.0, alignment: .center)
                        .clipShape(Circle())
                        .overlay(Circle().stroke(Color.white, lineWidth: 4))
                        .shadow(radius: 10)
                        .offset(y: -50)

                    HStack {
                        NavigationLink(destination: LoginView()) {
                             HStack {
                                 Text("Login")
                                     .fontWeight(.semibold)
                             }
                             .padding()
                             .foregroundColor(.white)
                             .background(LinearGradient(gradient: Gradient(colors: [Color.red, Color.purple]), startPoint: .leading, endPoint: .trailing))
                             .cornerRadius(40)
                         }.padding().offset(y: 100)

                         NavigationLink(destination: UserView()) {
                             HStack {
                                 Text("Sign Up")
                                     .fontWeight(.semibold)
                             }
                             .padding()
                             .foregroundColor(.white)
                             .background(LinearGradient(gradient: Gradient(colors: [Color.red, Color.purple]), startPoint: .leading, endPoint: .trailing))
                             .cornerRadius(40)
                         }.padding().offset(y: 100)
                    }

                }
                .navigationBarTitle(Text("Side Effects"))
            }
        }
    }
}

struct ContentView_Previews: PreviewProvider {
    static var previews: some View {
        ContentView()
    }
}
